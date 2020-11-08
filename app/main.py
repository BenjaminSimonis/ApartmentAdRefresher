from constants import url
from selenium import webdriver

options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

browser = webdriver.Firefox(options=options)
 
browser.get(url)
 
browser.save_screenshot('headless_firefox_test.png')
 
browser.quit()