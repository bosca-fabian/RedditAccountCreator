from selenium import webdriver

from selenium.webdriver.common.by import By

import time
from random import randint
import requests


def captchaSolver(driver):

    print('Solving captcha...')
    # time.sleep(randint(10, 15))
    apiKey = ''  # Add your API key here!
    siteKey = ''
    pageUrl = 'https://www.reddit.com/register/'
    requestUrl = 'https://2captcha.com/in.php?key=' + apiKey + '&method=userrecaptcha&googlekey=' + siteKey + '&pageurl=' + pageUrl
    print('Requesting 2captcha API...')
    resp = requests.get(requestUrl)
    if (resp.text[0:2] != 'OK'):
        print('Service error has occured. Error code: ' + resp.text)
        return
    captchaId = resp.text[3:]
    print(
        'Submitted request successfully, waiting for 30 seconds until requesting return...')
    time.sleep(30)
    returnUrl = 'https://2captcha.com/res.php?key=' + apiKey + '&action=get&id=' + captchaId
    print('Requesting return...')
    resp = requests.get(returnUrl)
    if resp.text == 'CAPCHA_NOT_READY':
        while resp.text == 'CAPCHA_NOT_READY':
            print('Captcha is not ready, requesting again in 5 seconds...')
            time.sleep(5)
            resp = requests.get(returnUrl)
    elif resp.text[0:5] == 'ERROR':
        print('Service error has occured. Error code: ' + resp.text)
        return
    ansToken = resp.text[3:]
    if ansToken == 'OR_CAPCHA_UNSOLVABLE':
        print('Service error has occured. Error code: ' + resp.text)
        return
    print('Answer token recieved: ' + ansToken)

    captchaInput = driver.find_element(by=By.XPATH, value='//*['
                                                          '@id="g-recaptcha-response"]')

    driver.execute_script("arguments[0].style.display = 'block';",
                          captchaInput)

    captchaInput.click()

    captchaInput.send_keys(ansToken)
