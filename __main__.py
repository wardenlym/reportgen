import os
from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

output_dir="/output"
if not os.path.isdir(output_dir):
    output_dir = "."
 
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

time.sleep(5)

print(driver.get_window_size())
driver.set_window_size(1920,1080)
driver.set_window_size(1680,900)
print(driver.get_window_size())

driver.save_screenshot(output_dir+'/screen.png')
 
driver.close()
 
end_time=time.time()
print('this is end_time ',end_time)

driver.quit()


from docx import Document

document = Document()
paragraph = document.add_paragraph('Lorem ipsum dolor sit amet.')
document.save(output_dir+'/weekly-report.docx')
