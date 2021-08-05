import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from personal_information import phone_number
from personal_information import password

import pyautogui as p
from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path="/geckodriver")

driver.get("https://tinder.com/app/recs")
driver.maximize_window()

time.sleep(10)
driver.execute_script('''window.open("https://www.facebook.com", "_blank");''')
time.sleep(10)

p.moveTo(1000, 635, 1)#cookie
p.mouseDown()
p.mouseUp()
time.sleep(5)
p.moveTo(1200, 280, 0.5)#username
p.mouseDown()
p.mouseUp()
p.write(phone_number)
time.sleep(5)


p.moveTo(1200, 350, 0.5)#password
p.keyDown('tab')
p.keyUp('tab')

p.write(password)




print("passatooooooooooooooo")



#per  accedeere a facebook
p.moveTo(1200, 400, 0.5)
p.mouseDown()
p.mouseUp()


submit_button = driver.find_element_by_css_selector(".Bdrs\(0\) > span:nth-child(1)")
submit_button.click()
time.sleep(10)




