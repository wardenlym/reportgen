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
# data=query(PROMETHEUS_SERVER,'promhttp_metric_handler_requests_total')
# print(json.dumps(data))


import os
from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
 
GRAFANA_API_KEY="eyJrIjoidGdvYkhyZTkxS1BldkoyVVZKdmQ4UUNiVGhMNlZUbWgiLCJuIjoid2Vla2x5LXJlcG9ydHMiLCJpZCI6MX0="

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('Authorization=Bearer eyJrIjoidGdvYkhyZTkxS1BldkoyVVZKdmQ4UUNiVGhMNlZUbWgiLCJuIjoid2Vla2x5LXJlcG9ydHMiLCJpZCI6MX0=')
 
base_url = "http://172.29.40.27:32001/d/sgrwz7XGz/test-weekly-report?orgId=1&refresh=30s"
headers = {
    'Authorization': 'Bearer %s' % GRAFANA_API_KEY
}

#对应的chromedriver的放置目录
driver = webdriver.Chrome(executable_path=("/usr/bin/chromedriver"), options=chrome_options)


def interceptor(request):
    request.headers['Authorization'] = 'Bearer %s' % GRAFANA_API_KEY

driver.request_interceptor = interceptor
driver.get(base_url + "/")
 
start_time=time.time()
print('this is start_time ',start_time)
 
# driver.find_element_by_id("kw").send_keys("admin")
# driver.find_element_by_id("kw").send_keys("admin")
# driver.find_element_by_id("su").click()

time.sleep(10)

print(driver.get_window_size())
driver.set_window_size(1920,1080)
print(driver.get_window_size())

driver.save_screenshot('screen.png')
 
driver.close()
 
end_time=time.time()
print('this is end_time ',end_time)

driver.quit()

