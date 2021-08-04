#codice per trovare i  codici a barre dei prodotti di PAM
import pyautogui as p

from selenium import webdriver
import urllib.request
#import telegram_bot
import signal, time
from selenium.webdriver.common.keys import Keys

from personal_information import log_facebook



class TimeoutError (RuntimeError):
    pass

def handler (signum, frame):
    raise TimeoutError()

def tinder(url):
    driver = webdriver.Firefox(executable_path="/tinder/geckodriver")
    driver.get(url)
    driver.maximize_window()

    log_facebook(driver)

    submit_button = driver.find_element_by_css_selector(".Bdrs\(0\) > span:nth-child(1)")
    submit_button.click()
    time.sleep(10)

    submit_button = driver.find_element_by_css_selector("div.My\(10px\):nth-child(2) > button:nth-child(1) > span:nth-child(2)")
    submit_button.click()
    time.sleep(30)

    submit_button = driver.find_element_by_css_selector("button.Ell:nth-child(1) > span:nth-child(1)")
    submit_button.click()
    time.sleep(10)
    submit_button = driver.find_element_by_css_selector("button.Ell:nth-child(1) > span:nth-child(1)")
    submit_button.click()
    time.sleep(60)
    p.moveTo(383, 190, 1)#accept position with your natural hand ;-)
    p.mouseDown()
    p.mouseUp()
    time.sleep(10)
    p.moveTo(600, 220, 1)#2
    p.mouseDown()
    p.mouseUp()

    submit_button = driver.find_element_by_css_selector("button.Ell:nth-child(1) > span:nth-child(1)")
    submit_button.click()

    time.sleep(10)
    p.moveTo(600, 180, 1)  # 2
    p.mouseDown()
    p.mouseUp()


    print("ACCEPT COOKIESSSSSSSSSSSSSSSSSSSS and active notifications with your natural hand ;-)")
    time.sleep(10)

    while True:
        try:
            submit_button = driver.find_element_by_css_selector("div.Mx\(a\):nth-child(4) > button:nth-child(1) > span:nth-child(1) > svg:nth-child(1) > path:nth-child(1)")
            submit_button.click()
            time.sleep(10)
        except:
            submit_button = driver.find_element_by_css_selector("button.button:nth-child(6) > span:nth-child(1)")
            submit_button.click()
            time.sleep(10)

    return



if __name__ == "__main__":
    tinder('https://tinder.com/app/recs')
