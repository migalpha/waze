from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import json

def foi(data: dict) -> dict:
    processed = {
        "id": data['id'],
        "roadType": data['roadType'],
        "validated": str(data['validated']).lower(),
        "updatedOn": data['updatedOn'],
        "geometry": data['geometry'],
        "fwdMaxSpeed": data['fwdMaxSpeed'],
        "revMaxSpeed": data['revMaxSpeed']
    }
    return processed

driver = webdriver.Firefox(executable_path=r'./geckodriver')
driver.get("https://www.waze.com/es/signin")
driver.find_element_by_name("username").send_keys("user")
driver.find_element_by_name("password").send_keys("pass")
driver.find_element_by_css_selector(".wz-button--primary-blue").click()
time.sleep(90)

segments = []

with open('./bboxes.json', 'r') as f_bbox:
    bboxes = json.load(f_bbox)
    for bb in bboxes['bboxes']:
        uri = f"https://www.waze.com/row-Descartes-live/app/Features?roadTypes=1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21&bbox={bb['e']},{bb['n']},{bb['w']},{bb['s']}&language=en-GB"
        print(uri)
        driver.get(uri)
        try:
            info = json.loads(driver.find_element_by_id("json").text)
            foi_data = list(map(foi, info['segments']['objects']))
            segments.extend(foi_data)
        except NoSuchElementException:  #spelling error making this code not work as expected
            pass

with open('./segments.json', 'w') as f:
    f.write(json.dumps(segments))
driver.close()
