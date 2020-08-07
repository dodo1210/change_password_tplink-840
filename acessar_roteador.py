#add libraries
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

#selenium configurations
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

#create and execute drive
driver = webdriver.Chrome(chrome_options=options,executable_path='./chromedriver')
a = driver.get("http://192.168.0.1")
time.sleep(2)

#add username
name = driver.find_element_by_id('userName')
name.send_keys('admin')

#add password
password = driver.find_element_by_id('pcPassword')
password.send_keys('doguinha2019')
time.sleep(2)

#make login
button = driver.find_element_by_id('loginBtn')
button.click()
time.sleep(2)

#focus for iframe
iframe = driver.find_element_by_id("frame1")
driver.switch_to.frame(iframe)

#menu options
li_element = driver.find_elements_by_css_selector('li.ml1')
li_element[3].click()

#menu options
li_element2 = driver.find_elements_by_css_selector('li.ml2')
li_element2[5].click()

#focus for other iframe
driver.switch_to.default_content()
iframe = driver.find_element_by_id("frame2")
driver.switch_to.frame(iframe)

#add password
inp_pass = driver.find_element_by_id('pskSecret')
inp_pass.click()
inp_pass.clear()
inp_pass.send_keys('(coffee).')

#click in button
inp_btn = driver.find_elements_by_css_selector('input.button.L.T.T_save')
inp_btn[0].click()

print("THE END")