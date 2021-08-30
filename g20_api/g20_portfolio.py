#!/usr/bin/env python
import traceback
import pandas as pd
import g20_dbHelper as dbHelper
import uuid

db = None
db5 = None
root_folder = 'files/g20/'
scenarios_map = {'Below 2oC':"Below 2oC", 'Current Policies':"Current policies", 'Delayed Transition':"Delayed transition"}
# scenario_list = ['Below 2oC', 'Current Policies', 'Delayed Transition']
scenario_list = []
model_scenario_list = []
year_list = ['2020', '2025', '2030', '2035', '2040', '2045', '2050']
aim_type_list = ['Portfolio', 'Sector']
# aim_type_list = [ 'Sector']
db_ver = 4
default_model = 'REMIND-MAgPIE 2.1-4.2_downscaled'


def process(loan_company, db_version=4):
    global db, db5, db_ver, scenario_list, model_scenario_list
    try:
        db_ver = db_version
        if db_version == 5:
            db5 = dbHelper.db_init_dm5()
        else:
            db = dbHelper.db_init()

        scenario_list = list(scenarios_map.keys())
        model_scenario_list = list(scenarios_map.values())

        loan_company['LoanValue'] = float(loan_company['LoanValue'])
        loan_company['GHGEmission'] = float(loan_company['GHGEmission'])

        cur = db5.reportdata.find(
            {'Company': loan_company['Company'], 'Scenario': {'$in': model_scenario_list}, 'Region': loan_company['CountryISO3'], 'Type': 'pd_average'})
        climate_pd_df = pd.DataFrame(list(cur))
        cur.close()

        unadjusted_pd_2020 = float(0)
        for scenario in scenario_list:
            indicator = '%s%s' % (scenario.replace(' ', ''), 'Climate')
            climate_pd = None
            if len(climate_pd_df) > 0:
                climate_pd = climate_pd_df[climate_pd_df.Scenario == scenarios_map[scenario]]

            if climate_pd is not None and len(climate_pd) > 0:
                cpd_data = climate_pd['Data'].iloc[0]
                unadjusted_pd_2020 = cpd_data[year_list[0]]
                # for year in year_list:
                #     indicator_doc[year] = cpd_data[year]
                indicator_doc = {year: cpd_data[year] for year in year_list }
            else:
                indicator_doc = {year: float(0) for year in year_list}
            loan_company[indicator] = [indicator_doc]

        # print('indicator_values:', indicator_values)
        loan_company['UnAdjustedPD'] = unadjusted_pd_2020

        #3. get data from db
        m_proj = {'_id': 0}
        for scenario in scenario_list:
            for atype in aim_type_list:
                field_name = '%s%s' % (scenario.replace(' ', ''), atype)
                m_proj[field_name] = 0
        if db_ver == 4:
            cur = db.CompanyPDData.find({'Company': {'$ne':loan_company['Company']}}, projection=m_proj)
        else:
            cur = db5.companypddata.find({'Company': {'$ne': loan_company['Company']}}, projection=m_proj)
        data_df_all = pd.DataFrame(list(cur))
        # print(data_df_all.head())
        cur.close()

        #4. calculate WACI-2020 value
        data_df_all = data_df_all.append(loan_company, ignore_index=True)
        data_df = data_df_all[['LoanValue', 'GHGEmission','UnAdjustedPD', 'Sector']].copy()
        loan_val = loan_company['LoanValue']
        ghg_emissions = loan_company['GHGEmission']
        # cmp_basic_data = {'LoanValue': loan_val, 'GHGEmission':ghg_emissions, 'UnAdjustedPD':unadjusted_pd_2020}
        # data_df = data_df.append(cmp_basic_data, ignore_index=True)
        print("data_df count after:", len(data_df))

        loan_sum = data_df["LoanValue"].sum()
        print('loan_sum:', loan_sum)
        WACI2020 = round(loan_val/loan_sum* ghg_emissions, 4)
        print('WACI2020:', WACI2020)
        loan_company['WACI2020'] = WACI2020
        # set WACI2020 to DB
        data_df_all.loc[data_df_all['Company'] == loan_company['Company'], 'WACI2020'] = WACI2020


        #5. calculate "Portfolio average -2020"
        data_df['Portfolio2020'] = data_df[['LoanValue', 'UnAdjustedPD']].apply(lambda x: x[0]*x[1], axis=1)
        # print('Portfolio2020:', data_df['Portfolio2020'])
        portfolio2020_sum = data_df['Portfolio2020'].sum()
        print('portfolio2020_sum:', portfolio2020_sum)
        portfolio2020_avg = round( portfolio2020_sum/loan_sum, 4)
        print('portfolio2020_avg:', portfolio2020_avg)

        # 6. calculate "Sector average -2020"
        # get_sectorid(loan_company)
        cmp_sector = loan_company['Sector']
        data_df_sector = data_df[data_df.Sector == cmp_sector].copy()
        loan_sum_sector = data_df_sector['LoanValue'].sum()
        print('sector count: ', len(data_df_sector))
        data_df_sector['Sector2020'] = data_df_sector[['LoanValue', 'UnAdjustedPD']].apply(lambda x: x[0] * x[1], axis=1)
        # print('Sector2020:', data_df_sector['Sector2020'].head(5))
        sector2020_sum = data_df_sector['Sector2020'].sum()
        print('sector2020_sum:', sector2020_sum)
        sector2020_avg = round( sector2020_sum/loan_sum_sector, 4)
        print('sector2020_avg:', sector2020_avg)


        #6. calc portfolio average under different scenarios
        # aim_type_list = ['Climate', 'Portfolio', 'Sector']

        for atype in aim_type_list:
            if atype == 'Portfolio':
                calc(data_df_all, data_df, atype, portfolio2020_avg, loan_company, loan_sum)
            else:
                calc(data_df_all[data_df_all.Sector == cmp_sector], data_df_sector, atype, sector2020_avg, loan_company, loan_sum_sector)
        if db_ver == 4:
            db.CompanyPDData.replace_one({'Company':loan_company['Company']}, loan_company, upsert=True)
        else:
            doc_count = db5.companypddata.count_documents({'Company': loan_company['Company']})
            if doc_count == 0:
                loan_company['_id'] = str(uuid.uuid4())
                db5.companypddata.insert_one(loan_company)
            else:
                db5.companypddata.replace_one({'Company': loan_company['Company']}, loan_company, upsert=True)
        print('finish')
        return loan_company
    except Exception as e:
        traceback.print_exc()
        raise


def calc(data_df_all, data_df, atype, type_avg_val, loan_company, loan_sum):
    try:
        for scenario in scenario_list:
            indicator_db = '%s%s' % (scenario.replace(' ', ''), atype)
            print('indicator_db:', indicator_db)
            doc = {'2020': type_avg_val}

            for year in year_list:
                filter_indicator = '%s%s' % (scenario.replace(' ', ''), 'Climate')
                print('filter_indicator:', filter_indicator)
                indicator_db_year = '%s%s' % (indicator_db, year)
                print('indicator_db_year:', indicator_db_year)
                data_df["indicator_db_years_json"] = data_df_all[filter_indicator].apply(
                    lambda d: {k: v for k, v in d[0].items()})
                # print('indicator_db_years_json df: ',  data_df["indicator_db_years_json"])

                year_val_df = pd.json_normalize(data_df['indicator_db_years_json'])
                data_df = pd.concat([data_df.reset_index(drop=True),year_val_df.reset_index(drop=True)], axis=1)
                # data_df[year_list] = pd.json_normalize(data_df['indicator_db_years_json'])
                # print(data_df.head())
                data_df[indicator_db_year] = data_df[['LoanValue', year]].apply(lambda x: x[0] * x[1], axis=1)
                sum_year = data_df[indicator_db_year].sum()
                avg = round(sum_year / loan_sum, 4)
                doc[year] = avg
            loan_company[indicator_db] = [doc]
        print("loan_company", loan_company)
    except Exception as e:
        traceback.print_exc()


def get_sectorid(loan_company):
    for row in db5.climate_drivers.find({'Sector':loan_company['Sector']}):
        loan_company['Sector'] = row['SectorID']


if __name__ == '__main__':
    company_doc = {"LoanAppID": '9ef4e620-fa7d-47f6-95e3-e801440d4163', "Company": "LafargeHolcim", "Sector": "Cement", "CountryISO3": "USA", "LoanValue": 450, "GHGEmission": 73}
    process(company_doc, db_version=5)
