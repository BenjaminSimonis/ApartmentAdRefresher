import time
import constants
import credentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def main():
    browser = get_headless_browser()
    try:
        time.sleep(constants.SLEEP_COUNTER)
        log_into_account(browser)
        time.sleep(constants.SLEEP_COUNTER)
        edit_apartment_ad(browser)
    finally:
        browser.quit()
        print("Browser closed")


def get_headless_browser():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--private')
    options.set_preference("javascript.enabled", True)

    browser = webdriver.Firefox(service=Service("/usr/local/bin/geckodriver"), options=options)
    browser.maximize_window()
    return browser


def log_into_account(browser):
    browser.get(constants.URL)
    time.sleep(constants.SLEEP_COUNTER)
    try:
        browser.find_element(By.XPATH, constants.COOKIE_ACCEPT).click()
        time.sleep(constants.SLEEP_COUNTER)
    except:
        print("Cookies already accepted")

    browser.find_element(By.CSS_SELECTOR, constants.LOGIN_BUTTON_CSS).click()
    time.sleep(constants.SLEEP_COUNTER)
    browser.find_element(By.XPATH, constants.LOGIN_NAME_PATH).send_keys(credentials.LOGIN_NAME)
    browser.find_element(By.XPATH, constants.LOGIN_PW_PATH).send_keys(credentials.LOGIN_PW)
    browser.find_element(By.XPATH, constants.LOGIN_FORM_BUTTON).click()
    time.sleep(constants.SLEEP_COUNTER)
    return True

def get_apartment_counter(browser):
    browser.get(constants.URL_ADS)
    time.sleep(constants.SLEEP_COUNTER)
    ad_text = browser.find_element(By.CSS_SELECTOR, constants.AD_COUNTER_FIELD_CSS).text
    ad_count = ad_text.split()
    return int(ad_count[0])

def edit_apartment_ad(browser):
    apartment_count = get_apartment_counter(browser)
    print(apartment_count)
    #EDIT_AD_BUTTON_PATH = constants.EDIT_AD_BUTTON0 if apartment_count == 1 else constants.EDIT_AD_BUTTON1

    for runner in range(apartment_count):
        adlist_number = runner + 1
        browser.get(constants.URL_ADS)
        time.sleep(constants.SLEEP_COUNTER)
        print("Ad Number: " + str(adlist_number))

        browser.find_element(By.XPATH, constants.EDIT_AD_BUTTON1 + str(adlist_number) + constants.EDIT_AD_BUTTON2).click()
        time.sleep(constants.SLEEP_COUNTER)
        browser.find_element(By.XPATH, constants.EDIT_AD_BUTTON1 + str(adlist_number) + constants.EDIT_AD_BUTTON3).click()

        time.sleep(constants.SLEEP_COUNTER)
        if is_element_present(browser, By.XPATH, constants.HARD_AD_LIMIT_XPATH):
            browser.execute_script("document.getElementById('hard_ad_limit_modal').style.display = 'none';")

        time.sleep(constants.SLEEP_COUNTER)
        description_field = browser.find_element(By.XPATH, constants.AD_DESCRIPTION_FIELD)
        description_field.send_keys(Keys.SPACE)
        description_field.send_keys(Keys.BACKSPACE)
        ActionChains(browser).send_keys(Keys.ESCAPE).perform()

        time.sleep(constants.SLEEP_COUNTER)
        if is_element_present(browser, By.XPATH, constants.PRIVATE_AD_MODAL_XPATH):
            browser.execute_script("document.getElementById('private_users_ad_modal').style.display = 'none';")

        time.sleep(constants.SLEEP_COUNTER)
        button = browser.find_element(By.XPATH, constants.SAVE_EDITED_AD_BUTTON)
        browser.execute_script("arguments[0].click();", button)
        print('Saved')
        time.sleep(constants.SLEEP_COUNTER)

    return True

def is_element_present(browser, by, value):
    try:
        browser.find_element(by, value)
        return True
    except:
        return False

if __name__ == '__main__':
    main()
