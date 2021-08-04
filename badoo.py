#codice per trovare i  codici a barre dei prodotti di PAM

from selenium import webdriver
import urllib.request
#import telegram_bot
import signal, time

from personal_information import log_facebook



class TimeoutError (RuntimeError):
    pass

def handler (signum, frame):
    raise TimeoutError()


def tinder(url):

    driver = webdriver.Firefox(executable_path="/tinder/geckodriver")
    driver.get(url)

    log_facebook(driver)
    time.sleep(10)
    submit_button = driver.find_element_by_css_selector("a.btn--block")
    submit_button.click()
    time.sleep(30)

    submit_button = driver.find_element_by_css_selector(".profile-action--color-yes")
    submit_button.click()
    time.sleep(10)
    submit_button = driver.find_element_by_css_selector(".btn--monochrome")
    submit_button.click()
    time.sleep(5)


    while True:
        try:
            descrizione = driver.find_element_by_css_selector('.profile-section__txt--about > p:nth-child(1)')
            if 'trans' in descrizione.text.lower() or 'travestita' in descrizione.text.lower() or 'travestito' in descrizione.text.lower() or 'gay' in descrizione.text.lower():
                button=driver.find_element_by_css_selector('.profile-action--color-no')
                button.click()
            else:
                submit_button = driver.find_element_by_css_selector(".profile-action--color-yes")
                submit_button.click()
                time.sleep(5)
        except:
            submit_button = driver.find_element_by_css_selector(".profile-action--color-yes")
            submit_button.click()
            time.sleep(5)


if __name__ == "__main__":
    tinder('https://badoo.com/encounters')
