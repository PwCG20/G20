#!/usr/bin/env python
from flask import Flask,  request
import json
# import g20_data_logic_v2 as data_service
# import g20_transition_risk_v2 as tr_service
import g20_portfolio as portfolio_service
import g20_climate_pd as tr_service
import traceback

app = Flask(__name__)


@app.route('/airtrace/api/processdm5', methods=["POST"])
def process_dm5():
    return_dict = get_return_doc()
    try:
        if len(request.get_data()) == 0:
            return_dict['code'] = '-1'
            return_dict['message'] = 'no parameters'

        req_data = request.get_data()
        load_company = json.loads(req_data, encoding='utf-8')
        print('processdm5_req_data: ', load_company)
        data = portfolio_service.process(load_company, db_version=5)
        return_dict['data'] = data
    except Exception as e:
        return_dict['code'] = -1
        return_dict['message'] = str(e)
        traceback.print_exc()
    return json.dumps(return_dict, ensure_ascii=False)


@app.route('/airtrace/api/transitionriskdm5', methods=["POST"])
def calcTransitionRisk_dm5():
    return_dict = get_return_doc()
    try:
        if len(request.get_data()) == 0:
            return_dict['code'] = '-1'
            return_dict['message'] = 'no parameters'

        req_data = request.get_data()
        loan_params = json.loads(req_data, encoding='utf-8')
        print('transitionriskdm5_req_data: ', loan_params)
        data = tr_service.transition_risk(loan_params)
        return_dict['data'] = data
    except Exception as e:
        return_dict['code'] = -1
        return_dict['message'] = str(e)
        traceback.print_exc()
    return json.dumps(return_dict, ensure_ascii=False)


@app.route('/airtrace/api/cleantransitionriskreport', methods=["POST"])
def clean_transition_risk():
    return_dict = get_return_doc()
    try:
        if len(request.get_data()) == 0:
            return_dict['code'] = '-1'
            return_dict['message'] = 'no parameters'

        req_data = request.get_data()
        param = json.loads(req_data, encoding='utf-8')
        print('clean_transition_risk: ', param['Company'])
        tr_service.clean_report(param['Company'])
    except Exception as e:
        return_dict['code'] = -1
        return_dict['message'] = str(e)
        traceback.print_exc()
    return json.dumps(return_dict, ensure_ascii=False)


def get_return_doc():
   return {'code': 0, 'message': '', 'data': None}


if __name__ == '__main__':
    app.run(port=5000)