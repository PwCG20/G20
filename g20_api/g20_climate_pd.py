import traceback
import pandas as pd
import g20_dbHelper as dbHelper
import numpy as py
import uuid
import g20_portfolio as pd_services
# from scipy.stats import norm

db = None
root_folder = 'files/g20/'
year_cols = None
models = {'GCAM5.3_NGFS_downscaled': 'GCMd', 'MESSAGEix-GLOBIOM 1.1_downscaled': 'MSGd', 'REMIND-MAgPIE 2.1-4.2_downscaled': 'RMPd'}
model_lst = []
model_df = None
scenarios = {'Below 2oC': '2DC', 'Current policies': 'CPO', 'Delayed transition': 'DET',
                 'Divergent Net Zero': 'DNZ', 'Nationally Determined Contributions (NDCs)': 'NDC',
                 'Net Zero 2050': 'NZ5', 'NiGEM NGFS v1.21 Base Scenario': 'NGM'}
scenario_lst = []
report_type = {'CO2 emissions':'Carbon cost', 'Electricity demand':'Electricity cost'}


def transition_risk(loan_params):
    global db, model_lst, scenario_lst, model_df
    db = dbHelper.db_init_dm5()
    get_cols()

    loan_app_id = loan_params['LoanAppID']
    scenario_param = loan_params['Scenario']
    loan_app = get_loan_company_info(loan_app_id)
    if loan_app is None:
        print('loan application does not exist')
        return 'loan application does not exist'
    loan_app['CountryISO3'] = loan_params['Region']


    rtl_doc_list = []
    rd_cur = db.reportdata.find({'Company': loan_app['Company'], 'Region': loan_app['CountryISO3'], "Scenario": scenario_param, 'Type': {'$in':['Carbon cost', 'Electricity cost', 'revenue_price', 'revenue']}})
    if rd_cur is not None:
        rtl_doc_list = list(rd_cur)
        rd_cur.close()
        if len(rtl_doc_list) > 0:
            return rtl_doc_list


    climate_driver = get_climate_driver(loan_app['Sector'])
    if climate_driver is None:
        return 'loan application sector is invalid'

    # get factor adjustment
    # adjustment_factors = get_adjustment()
    # revenue_adjust = adjustment_factors[adjustment_factors['Type'] == 'Revenue']

    # tmp_scenario_lst = [scenario_param]
    tmp_scenario_lst = ['Below 2oC', 'Current policies', 'Delayed transition']
    if scenario_param not in tmp_scenario_lst:
        tmp_scenario_lst.append(scenario_param)

    model_lst = list(models.keys())
    model_df = pd.DataFrame(model_lst, columns=['Model'])
    model_df.sort_values(by=['Model'], inplace=True)
    # print(model_df.head())
    # scenario_lst = list(scenarios.keys())
    loan_amount = loan_app['LoanValue']
    for scenario in tmp_scenario_lst:
        try:
            revenue_adjust = get_physical_risk_adjustment_factor_revenue(loan_app, scenario)

            carbon_cost = calc_carbon_cost(loan_app, scenario, climate_driver,  (rtl_doc_list if scenario == scenario_param else None) )
            electricity_cost = calc_electricity_cost(loan_app, scenario, climate_driver, (rtl_doc_list if scenario == scenario_param else None))
            # if carbon_cost is None or electricity_cost is None:
            if carbon_cost is None or electricity_cost is None or (len(carbon_cost) == 0 and len(electricity_cost) == 0):
                print('carbon_cost or electricity_cost is none')
                continue

            # print(rtl_doc_list)
            revenue = calc_revenue(loan_app, scenario, climate_driver, revenue_adjust, (rtl_doc_list if scenario == scenario_param else None))

            ni_new = calc_net_income_impact(loan_app, revenue, carbon_cost, electricity_cost, scenario)
            cl_new, weight_cl, weight_ll, company_tl  = calc_current_liabilities_impact(loan_app, ni_new, scenario)
            tl_new = calc_total_liabilities_impact(loan_app, weight_cl, weight_ll, company_tl, ni_new, scenario)
            # calc_total_assets_impact
            company_ta = loan_app['TotalAssets'] + loan_amount

            # Apply impact to Current Assets
            company_ca = loan_app['CurrentAssets'] + loan_amount

            unadjusted_pd = calc_climate_pd(loan_app, ni_new, tl_new, cl_new, scenario, company_ta, company_ca)
            print("unadjusted_pd: ", unadjusted_pd)

        except Exception as e:
            traceback.print_exc()
            raise
    # print('result: ', rtl_doc_list)

    calc_sector_avg(loan_app)
    return rtl_doc_list


def calc_sector_avg(loan_app):
    try:
        loan_company = {"LoanAppID": loan_app['_id'], "Company": loan_app['Company'],
                        "Sector":loan_app['Sector'], "CountryISO3": loan_app['CountryISO3'],
                        "LoanValue": loan_app['LoanValue'], "GHGEmission": loan_app['GHGEmissions']}
        print('calc_sector_avg: ', loan_app)
        pd_services.process(loan_company, db_version=5)
    except Exception as e:
        traceback.print_exc()


def get_physical_risk_adjustment_factor_revenue(loan_app, scenario):
    m_filter = {'Variable':'Diagnostics|Macro-Economic Climate Damage|GDP Change %', 'Region': loan_app['CountryISO3'], 'Model':'REMIND-MAgPIE 2.1-4.2 IntegratedPhysicalDamages (median)',"Scenario":scenario}
    m_proj = {y: 1 for y in year_cols}
    cur = db.modeldata.find(m_filter, projection = m_proj)
    revenue_adjust = pd.DataFrame(list(cur), columns=year_cols)
    if revenue_adjust.shape[0] == 0:
       revenue_adjust.loc[revenue_adjust.shape[0]] = [None for y in year_cols]
    else:
        revenue_adjust.drop_duplicates(inplace=True)
    revenue_adjust['Type'] = 'Revenue'
    print(revenue_adjust.head())
    return revenue_adjust


def calc_carbon_cost(loan_app, scenario, climate_driver, rtl_doc_list):
    print("calc_carbon_cost: ")
    carbon_price_var = climate_driver['CarbonPrice']
    emission_var = climate_driver['EmissionsGrowth']
    country_iso3 = loan_app['CountryISO3']
    company_emissions = loan_app['GHGEmissions']
    m_proj = {'_id':0, 'Database':0, 'Region':0, 'Variable':0, 'Unit':0, 'batch':0}
    md_cur = db.modeldata.find({'Variable':carbon_price_var, 'Region': country_iso3, 'Model':{'$in':model_lst},"Scenario":scenario}, projection=m_proj)
    carbon_price = pd.DataFrame(list(md_cur))
    # print(carbon_price.head())
    md_cur.close()

    # m_proj = {'_id': 0, 'Database': 0, 'Region': 0}
    emission_cur = db.modeldata.find({'Variable':emission_var, 'Region': country_iso3, 'Model':{'$in':model_lst},"Scenario":scenario}, projection=m_proj)
    emission = pd.DataFrame(list(emission_cur))
    emission_cur.close()
    emission.drop_duplicates(inplace=True)
    # print(emission)

    if len(emission) == 0:
        return pd.DataFrame(columns = get_cost_cols())
    emission.drop(columns=['UniqueID', 'Scenario'], inplace=True)
    carbon_cost = pd.merge(carbon_price, emission, how='inner', on='Model')
    # print(carbon_cost.head())

    drop_cols = []
    for idx, year in enumerate(year_cols):
        drop_cols.append(year+'_x')
        drop_cols.append(year + '_y')
        if idx == 0:
            carbon_cost[year] = company_emissions * carbon_cost[year + '_x']
        else:
            carbon_cost[year] = company_emissions * carbon_cost[year + '_y'] / carbon_cost[ year_cols[0] + '_y'] * carbon_cost[year + '_x']

    carbon_cost.drop(columns=drop_cols, inplace=True)
    # print(carbon_cost.head())

    carbon_cost.sort_values(by=['Model'], inplace=True)
    save_report(carbon_cost, 'Carbon cost', scenario, loan_app, rtl_doc_list)
    return carbon_cost


def calc_electricity_cost(loan_app, scenario, climate_driver, rtl_doc_list):
    print('calc_electricity_cost: ')
    electricity_price_var = climate_driver['ElectricityPrice']
    electricity_var = climate_driver['ElectricityUse']
    country_iso3 = loan_app['CountryISO3']
    company_energyuse = loan_app['EnergyUse']
    m_proj = {'_id': 0, 'Database': 0, 'Region': 0, 'Variable': 0, 'Unit': 0, 'batch':0}
    md_cur = db.modeldata.find(
        {'Variable': electricity_price_var, 'Region': country_iso3, 'Model': {'$in': model_lst}, "Scenario": scenario},
        projection=m_proj)
    electricity_price = pd.DataFrame(list(md_cur))
    # print(electricity_price .head())
    md_cur.close()
    electricity_price.drop_duplicates(inplace=True)

    # m_proj = {'_id': 0, 'Database': 0, 'Region': 0}
    electricity_cur = db.modeldata.find(
        {'Variable': electricity_var, 'Region': country_iso3, 'Model': {'$in': model_lst}, "Scenario": scenario},
        projection=m_proj)
    electricity_use = pd.DataFrame(list(electricity_cur))
    electricity_cur.close()
    electricity_use.drop_duplicates(inplace=True)
    print(electricity_use)

    if len(electricity_use) == 0:
        return pd.DataFrame(columns = get_cost_cols())
    electricity_use.drop(columns=['UniqueID', 'Scenario'], inplace=True)
    electricity_cost = pd.merge(electricity_price, electricity_use, how='inner', on='Model')
    # print(electricity_cost.head())

    drop_cols = []
    for idx, year in enumerate(year_cols):
        drop_cols.append(year + '_x')
        drop_cols.append(year + '_y')
        if idx == 0:
            electricity_cost[year] = company_energyuse * electricity_cost[year + '_x'] * 1000
        else:
            electricity_cost[year] = company_energyuse * electricity_cost[year + '_y'] / electricity_cost[year_cols[0] + '_y'] * \
                                electricity_cost[year + '_x'] * 1000

    electricity_cost.drop(columns=drop_cols, inplace=True)
    # print(electricity_cost.head())

    electricity_cost.sort_values(by=['Model'], inplace=True)
    save_report(electricity_cost, 'Electricity cost', scenario, loan_app, rtl_doc_list)
    return electricity_cost


def calc_revenue(loan_app, scenario, climate_driver, revenue_adjust, rtl_doc_list):
    print('calc_revenue: ')
    revenue_var = climate_driver['DemandGrowth']
    company_revenue = loan_app['Revenue']
    country_iso3 = loan_app['CountryISO3']
    m_proj = {'_id': 0, 'Database': 0, 'Region': 0, 'Variable': 0, 'Unit': 0, 'batch':0}
    md_cur = db.modeldata.find(
        {'Variable': revenue_var, 'Region': country_iso3, 'Model': {'$in': model_lst}, "Scenario": scenario},
        projection=m_proj)
    demand = pd.DataFrame(list(md_cur))
    demand.drop_duplicates(inplace=True)
    demand = pd.merge(model_df, demand, how='left', on="Model")
    # print(demand.head())
    md_cur.close()

    # revenue price
    price_var = climate_driver['Price']
    md_cur = db.modeldata.find(
        {'Variable': price_var, 'Region': country_iso3, 'Model': {'$in': model_lst}, "Scenario": scenario},
        projection=m_proj)
    price = pd.DataFrame(list(md_cur))
    price.drop_duplicates(inplace=True)
    # print(price.head())
    md_cur.close()
    save_report(price, 'revenue_price', scenario, loan_app, rtl_doc_list)

    price.drop(columns=['UniqueID', 'Scenario'], inplace=True)
    revenue = pd.merge(price, demand, how='right', on='Model')
    drop_cols = []
    fst_year = year_cols[0]
    for idx, year in enumerate(year_cols):
        drop_cols.append(year + '_x')
        drop_cols.append(year + '_y')
        if idx == 0:
            revenue[year] = company_revenue
        else:
            revenue[year] = company_revenue * revenue[year + '_y'] / revenue[fst_year + '_y'] * revenue[year + '_x'] / revenue[fst_year + '_x'] * (1- pd.to_numeric(revenue_adjust.iloc[0][year])/100)
    revenue.drop(columns=drop_cols, inplace=True)
    # revenue.fillna(float(0), inplace=True)
    # print(revenue.columns)
    # print(revenue.head())
    revenue.sort_values(by=['Model'], inplace=True)
    save_report(revenue, 'revenue', scenario, loan_app, rtl_doc_list)
    return revenue


def calc_net_income_impact(loan_app, revenue, carbon_cost, electricity_cost, scenario):
    print("calc_net_income_impact: ")
    company_ni = loan_app['NetIncome']
    # ni_new = pd.DataFrame()
    # ni_new['Model'] = revenue['Model']
    ni_new = model_df.copy()
    fst_year = year_cols[0]
    for idx, year in enumerate(year_cols):
        if idx == 0:
            ni_new[year] = company_ni
        else:
            ni_new[year] = company_ni + (revenue[year] - revenue[fst_year]) * 0.1 - (carbon_cost[year] - carbon_cost[fst_year]) - (electricity_cost[year] - electricity_cost[fst_year]) * 0.1
    # print(ni_new.head())
    ni_new.sort_values(by=['Model'], inplace=True)
    save_report(ni_new, 'net_income', scenario, loan_app, None)
    return ni_new


def calc_current_liabilities_impact(loan_app, ni_new, scenario):
    print("calc_current_liabilities_impact: ")
    company_ta = loan_app['TotalAssets']
    company_cl = loan_app['CurrentLiabilities']
    weight_cl = company_cl /company_ta

    company_tl = loan_app['TotalLiabilities']
    company_ll = company_tl - company_cl
    weight_ll = company_ll / company_ta

    weight_equity = 1 - weight_cl - weight_ll
    cl_new = model_df.copy()
    fst_year = year_cols[0]
    for idx, year in enumerate(year_cols):
        if idx == 0:
            cl_new[year] = company_cl
        else:
            cl_new[year] = company_cl - (ni_new[year] - ni_new[fst_year]) * weight_cl
    # print(cl_new.head())
    cl_new.sort_values(by=['Model'], inplace=True)
    save_report(cl_new, 'current_liabilities', scenario, loan_app, None)
    return cl_new, weight_cl, weight_ll, company_tl


def calc_total_liabilities_impact(loan_app, weight_cl, weight_ll, company_tl, ni_new, scenario):
    print("calc_total_liabilities_impact: ")
    weight_tl = weight_cl + weight_ll
    loan_amount = loan_app['LoanValue']
    company_tl = company_tl + loan_amount
    tl_new = model_df.copy()
    fst_year = year_cols[0]
    for idx, year in enumerate(year_cols):
        if idx == 0:
            tl_new[year] = company_tl
        else:
            tl_new[year] = company_tl - (ni_new[year] - ni_new[fst_year]) * weight_tl
    # print(tl_new.head())
    tl_new.sort_values(by=['Model'], inplace=True)
    save_report(tl_new, 'total_liabilities', scenario, loan_app, None)
    return tl_new


def calc_climate_pd(loan_app, ni_new, tl_new, cl_new, scenario, company_ta, company_ca):
    # NI/TA
    print('calc_climate_pd: roa_df')
    roa = model_df.copy()
    for year in year_cols:
        roa[year] = ni_new[year] / company_ta
    # print(roa.head())

    # TL/TA
    print('calc_climate_pd: leverage')
    leverage = model_df.copy()
    for idx, year in enumerate(year_cols):
        leverage[year] = tl_new[year] / company_ta
    # print(leverage.head())
    save_report(leverage, 'leverage', scenario, loan_app, None)

    # CA/CL
    print('calc_climate_pd: liquidity')
    liquidity = model_df.copy()
    for year in year_cols:
        liquidity[year] = company_ca / cl_new[year]
    # print(liquidity.head())
    save_report(liquidity, 'liquidity', scenario, loan_app, None)

    # pd
    print('calc_climate_pd: PD')
    PD = model_df.copy()
    for year in year_cols:
        PD[year] = 1 / (1 + py.exp(-(-4.336 - 4.513 * roa[year] + 5.679 * leverage[year] + 0.004 * liquidity[year]))) * 0.1
    # print(PD.head())
    unadjusted_pd = PD['2020'].iloc[0]
    save_report(PD, 'pd', scenario, loan_app, None)

    # pd average
    if len(PD) > 0:
        pd_avg_doc = {"Model":""}
        for year in year_cols:
            pd_avg_doc[year] = PD[year].mean()
        save_report(pd.DataFrame([pd_avg_doc]), 'pd_average', scenario, loan_app, None)
    return unadjusted_pd


def get_climate_driver(sector):
    cur = db.climate_drivers.find({'Sector': sector})
    if cur is not None:
        climate_driver = list(cur)[0]
        cur.close()
    return climate_driver


def save_report(df, type, scenario, loan_app, rtl_doc_list):
    data_df = df.fillna(float(0))
    for (idx, row) in data_df.iterrows():
        # doc = dict(row)
        report = get_transition_risk_report_doc(loan_app['_id'], loan_app['Company'], loan_app['CountryISO3'], row['Model'], scenario, type)
        m_filter = report.copy()
        del m_filter['Company']
        del m_filter['Data']
        data = {}
        for year in year_cols:
            data[year] = row[year]
        report['Data'] = data
        doc_count = db.reportdata.count_documents(m_filter)
        if doc_count == 0:
            report['_id'] = str(uuid.uuid4())
            db.reportdata.insert_one(report)
        else:
            db.reportdata.replace_one(m_filter, report, upsert=True)

        if rtl_doc_list is not None:
            rtl_doc_list.append(report)


def get_transition_risk_report_doc(loan_app_id, company, region, model, scenario, type):
    return {
            "LoanAppID": loan_app_id,
            "Company": company,
           "Region": region,
           "Model": model,
           "Scenario": scenario,
           "Type": type,
           "Data": []
           }


def get_loan_company_info(loan_app_id):
    loan_app = None
    tmp = {'_id': loan_app_id}
    print(tmp)
    for row in db.loanapplication.find({'_id': loan_app_id}):
        loan_app = {'_id': loan_app_id, 'Company': row['CompanyName'], 'CountryISO3': row['CompanyISO3'], 'GHGEmissions': float(row['GHGEmissions']),
                    'ElectricityUse': float(row['ElectricityUse']), 'Sector': row['Sector'][0]['SectorID'], 'LoanValue': float(row['LoanValue']),
         'TotalAssets': float(row['TotalAssets']), 'TotalLiabilities': float(row['TotalLiabilities']), 'EBIT': float(row['EBIT']), 'CurrentLiabilities': float(row['CurrentLiabilities']),
         'CurrentAssets': float(row['CurrentAssets']), 'NetAssetValue': float(row['NetAssetValue']), 'NetIncome': float(row['NetIncome']), 'Revenue': float(row['Revenue'])}
        loan_app['EnergyUse'] = loan_app['ElectricityUse']*3.6/1000000000
    return loan_app


def get_cost_cols():
   return ['UniqueID', 'Model', 'Scenario'] + year_cols


def get_adjustment():
    cur = db.adjustment.find({})
    data_df = pd.DataFrame(list(cur))
    cur.close()
    return data_df


def get_cols():
    global year_cols
    year_cols = []
    for num in range(2020, 2055, 5):
        year_cols.append(str(num))


def clean_report(company_name):
    global db
    db = dbHelper.db_init_dm5()
    db.reportdata.delete_many({"Company": company_name})


if __name__ == '__main__':
    tmp = {"Scenario": "Nationally Determined Contributions (NDCs)", "Region": "USA", "LoanAppID": "9ef4e620-fa7d-47f6-95e3-e801440d4163"}
    lst = transition_risk(tmp)
    # print(lst)