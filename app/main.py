import time
import constants
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import subprocess


def main():
    browser = get_headless_browser()
    try:
        log_into_account(browser)
        edit_apartment_ad(browser)
    finally:
        browser.close
        browser.quit
        print("browser closed")

        # Kill all remaining firefox processes
        pids = str(subprocess.check_output(
            ['pidof', 'firefox-esr'])).split(' ')
        for ids in pids:
            ff_id = str(ids).replace("b'", "").replace("\\n'", "")
            subprocess.call(['kill', str(ff_id)])


def get_headless_browser():
    options = webdriver.FirefoxOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    executable_path = constants.GECKODRIVER_PATH
    browser = webdriver.Firefox(
        executable_path=executable_path, options=options)
    return browser


def log_into_account(browser):
    browser.get(constants.URL)
    time.sleep(constants.SLEEP_COUNTER)
    try:
        browser.find_element_by_xpath(constants.COOKIE_ACCEPT).click()
        time.sleep(constants.SLEEP_COUNTER)
    except:
        print("Cookies already accepted")
    browser.find_element_by_css_selector(constants.LOGIN_BUTTON_CSS).click()
    time.sleep(constants.SLEEP_COUNTER)
    browser.find_element_by_xpath(
        constants.LOGIN_NAME_PATH).send_keys(constants.LOGIN_NAME)
    browser.find_element_by_xpath(
        constants.LOGIN_PW_PATH).send_keys(constants.LOGIN_PW)
    browser.find_element_by_xpath(constants.LOGIN_FORM_BUTTON).click()
    time.sleep(constants.SLEEP_COUNTER)
    return True


def get_apartment_counter(browser):
    browser.get(constants.URL_ADS)
    time.sleep(constants.SLEEP_COUNTER)
    return int(browser.find_element_by_css_selector(constants.AD_COUNTER_FIELD_CSS).text)


def edit_apartment_ad(browser):
    apartment_count = get_apartment_counter(browser)
    print(apartment_count)

    for runner in range(apartment_count):
        adlist_number = runner + 1
        browser.get(constants.URL_ADS)
        time.sleep(constants.SLEEP_COUNTER)
        print("Ad Number: " + str(adlist_number))

        # Open Apartmant Ad from your list
        browser.find_element_by_xpath(
            constants.EDIT_AD_BUTTON1 + str(adlist_number) + constants.EDIT_AD_BUTTON2).click()
        time.sleep(constants.SLEEP_COUNTER)
        browser.find_element_by_xpath(
            constants.EDIT_AD_BUTTON1 + str(adlist_number) + constants.EDIT_AD_BUTTON3).click()

        # Edit ad description with one letter and delete it to make it look updated
        time.sleep(constants.SLEEP_COUNTER)
        browser.find_element_by_xpath(
            constants.AD_DESCRIPTION_FIELD).send_keys(Keys.SPACE)
        browser.find_element_by_xpath(
            constants.AD_DESCRIPTION_FIELD).send_keys(Keys.BACKSPACE)

        # Save ad
        browser.find_element_by_xpath(constants.SAVE_EDITED_AD_BUTTON).click()
        time.sleep(constants.SLEEP_COUNTER)

    return True


if __name__ == '__main__':
    main()
