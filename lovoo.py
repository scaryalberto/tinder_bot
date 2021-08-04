#codice per trovare i  codici a barre dei prodotti di PAM

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
import pyautogui as p


def tinder(url):
    driver = webdriver.Firefox(executable_path="/tinder/geckodriver")
    driver.get(url)
    driver.maximize_window()
    p.moveTo(1200, 775, 1)  # cookie
    p.mouseDown()
    p.mouseUp()
    time.sleep(10)
    log_facebook(driver)
    #after accept cookies start this part of code
    time.sleep(30)
    submit_button = driver.find_element_by_css_selector("button.o-button:nth-child(3)")
    submit_button.click()
    time.sleep(10)

    submit_button = driver.find_element_by_css_selector("button.o-button--facebook:nth-child(3)")
    submit_button.click()
    time.sleep(60)#insert password event

    submit_button = driver.find_element_by_css_selector("ul.o-nav:nth-child(1) > li:nth-child(2) > a:nth-child(1)")
    submit_button.click()
    time.sleep(5)

    while True:
        try:#does like
            submit_button = driver.find_element_by_css_selector(
                ".fa-heart")
            submit_button.click()
            time.sleep(5)
            print("I'm clicking")
        except:
            submit_button = driver.find_element_by_css_selector(
                ".fa-heart")
            submit_button.click()
            time.sleep(5)

    return

if __name__ == "__main__":
    tinder('https://it.lovoo.com/match')
