from prometheus_client import start_http_server, Summary
import requests
import random
import time
import json

PROMETHEUS_SERVER='http://172.29.40.27:32005'
PROMETHEUS_V1_API=PROMETHEUS_SERVER+'/api/v1'

PROMETHEUS_API=PROMETHEUS_V1_API
PROMETHEUS_API_target=PROMETHEUS_API+'/targets'
PROMETHEUS_API_query=PROMETHEUS_API+'/query?query='

# print('report gen')

def getTargetsStatus(address):
    url = address + '/api/v1/targets'
    response = requests.request('GET', url)
    if response.status_code == 200:
        targets = response.json()['data']['activeTargets']
        aliveNum, totalNum = 0, 0
        downList = []
        for target in targets:
            totalNum += 1
            if target['health'] == 'up':
                aliveNum += 1
            else:
                downList.append(target['labels']['instance'])
        print('-----------------------TargetsStatus--------------------------')
        print(str(aliveNum) + ' in ' + str(totalNum) + ' Targets are alive !!!')
        print('--------------------------------------------------------------')
        for down in downList:
            print('\033[31m\033[1m' + down + '\033[0m' + ' down !!!')
        print('-----------------------TargetsStatus--------------------------')
    else:
        print('\033[31m\033[1m' + 'Get targets status failed!' + '\033[0m')


def query(address, expr):
    url = address + '/api/v1/query?query=' + expr
    try:
        return json.loads(requests.get(url=url).content.decode('utf8', 'ignore'))
    except Exception as e:
        print(e)
        return {}

# getTargetsStatus(PROMETHEUS_SERVER)
data=query(PROMETHEUS_SERVER,'promhttp_metric_handler_requests_total')
print(json.dumps(data))
