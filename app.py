import os
import json
import requests
import operator
from flask import Flask, render_template, request
from collections import Counter
import logging
import pdb

app = Flask(__name__)


def package_response(result, result_code, error_msg=''):
    response = {}
    response['code'] = result_code
    response['msg'] = error_msg
    response['data'] = result
    return response

@app.route('/senti_pred/', methods=['POST'])
def senti_pred():

    headers = request.headers

    pdb.set_trace()
    ''' handle input is a json
    payload = json.loads(request.get_data().decode('utf-8'))
    logger.info('POST request: %s' % payload)

    queryText = payload.get('text', None)
    '''
    # assume input is (key, value) pair

    queryText = request.args['text']

    
    # result here is a dict
    result = {
            'pos':0.4,
            'neu':0.4,
            'neg':0.2
            }

    response = package_response(result, 0)
    #return json.dumps(result, ensure_ascii=False).encode('utf-8')
    return json.dumps(response, ensure_ascii=False).encode('utf-8')

if __name__ == '__main__':
    app.run()
