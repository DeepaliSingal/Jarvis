from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import pyttsx3
import speech_recognition as SR
from requests import get
from webdriver_manager.chrome import ChromeDriverManager

def start(email,password):
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.linkedin.com/login/")

        username_xpath='//*[@id="username"]'
        password_xpath='//*[@id="password"]'
        login_xpath='//*[@id="organic-div"]/form/div[3]/button'

        time.sleep(2)

        driver.find_element_by_xpath(username_xpath).send_keys(email)
        time.sleep(1)
        driver.find_element_by_xpath(password_xpath).send_keys(password)
        time.sleep(1)
        driver.find_element_by_xpath(login_xpath).click()
        return True
    except:
        return False