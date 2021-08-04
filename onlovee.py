#https://onlovee.com/profile_view.php


from selenium import webdriver
import urllib.request
#import telegram_bot
import signal, time
from selenium.webdriver.common.keys import Keys
from personal_information import onlovee_user, onlovee_password

class TimeoutError (RuntimeError):
    pass

def handler (signum, frame):
    raise TimeoutError()




def tinder(url):
    #    telegram_bot.telegram_bot_sendtext(message)

    driver = webdriver.Firefox(executable_path="/geckodriver")
    #signal.signal(signal.SIGALRM, handler)
    driver.get(url)

    #signal.alarm(30)  # dopo quanti secondi scatta il timer

    #time.sleep(5)


    time.sleep(30)
    submit_button = driver.find_element_by_css_selector(".cookie-popup-accept-cookies-btn")
    submit_button.click()#accetta i cookie
    time.sleep(30)

    #spri facebook
    submit_button = driver.find_element_by_css_selector("#pp_sign_in_open")
    submit_button.click()
    time.sleep(5)#inserisci la password

    #metti la mail
    submit_button = driver.find_element_by_css_selector("#form_login_user")
    submit_button.send_keys(onlovee_user)
    #submit_button.click()
    time.sleep(2)
    #metti la password
    submit_button = driver.find_element_by_css_selector("#form_login_pass")
    submit_button.send_keys(onlovee_password)
    #submit_button.click()
    time.sleep(2)
    submit_button = driver.find_element_by_css_selector("#form_login_submit")
    submit_button.click()
    time.sleep(10)
    submit_button = driver.find_element_by_css_selector("#narrow_menu_link_46")
    submit_button.click()
    time.sleep(10)

    while True:
        try:
            submit_button = driver.find_element_by_css_selector(".lgreen")
            submit_button.click()
            time.sleep(10)
        except:
            submit_button = driver.find_element_by_css_selector(".lgreen")
            submit_button.click()
            time.sleep(10)


if __name__ == "__main__":
    tinder('https://onlovee.com/')
