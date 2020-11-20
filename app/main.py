import time
import random
import constants
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def main():
    browser = get_headless_browser()
    log_into_account(browser)
    #edit_apartment_ad(browser)
    logout_account(browser)


def get_headless_browser():
    options = webdriver.FirefoxOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    browser = webdriver.Firefox(options=options)
    return browser


def log_into_account(browser):
    browser.get(constants.URL)
    browser.find_element_by_xpath(constants.LOGIN_BUTTON).click()
    time.sleep(2)
    browser.find_element_by_xpath(constants.LOGIN_NAME_PATH).send_keys(constants.LOGIN_NAME)
    browser.find_element_by_xpath(constants.LOGIN_PW_PATH).send_keys(constants.LOGIN_PW)
    browser.find_element_by_xpath(constants.LOGIN_FORM_BUTTON).click()
    browser.save_screenshot('test2.png')
    return True


def edit_apartment_ad(browser):
    browser.find_element_by_xpath(constants.EDIT_AD_BUTTON).click()
    # Edit ad description with one letter and delete it to make it look updated
    browser.find_element_by_xpath(constants.AD_DESCRIPTION_FIELD).send_keys(Keys.SPACE)
    browser.find_element_by_xpath(constants.AD_DESCRIPTION_FIELD).send_keys(Keys.BACKSPACE)
    # Save ad
    browser.find_element_by_xpath(constants.SAVE_EDITED_AD_BUTTON).click()
    time.sleep(2)
    return True


def logout_account(browser):
    browser.quit()
    return True


if __name__ == '__main__':
    while True:
        #Repeat every 22 to 36 hours
        time.sleep(random.randint(79200, 129600))
        main()
