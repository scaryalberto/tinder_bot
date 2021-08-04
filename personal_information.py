
import pyautogui as p

from selenium import webdriver
import urllib.request
#import telegram_bot
import signal, time
from selenium.webdriver.common.keys import Keys



phone_number=''
password=''
onlovee_user=''#onlovee doesn't have log in with facebook at the moment
onlovee_password=''

def log_facebook(driver):
    time.sleep(10)
    driver.execute_script('''window.open("https://www.facebook.com", "_blank");''')
    time.sleep(30)
    p.moveTo(1000, 635, 1)  # cookie
    p.mouseDown()
    p.mouseUp()
    time.sleep(5)
    p.moveTo(1200, 280, 0.5)  # username
    p.mouseDown()
    p.mouseUp()
    p.write(phone_number)
    time.sleep(5)
    p.moveTo(1200, 350, 0.5)  # password
    p.keyDown('tab')
    p.keyUp('tab')
    p.write(password)
    p.moveTo(1200, 400, 0.5)
    p.mouseDown()
    p.mouseUp()
    time.sleep(5)
    p.moveTo(50, 45, 0.5)
    p.mouseDown()
    p.mouseUp()
