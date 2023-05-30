import os
import time

from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver


def get_chrome_driver(config: dict, load_extension:False) -> WebDriver:
    options = chrome_options()
    if load_extension:
        options.add_extension(os.path.join(config["chromedriver_path"], config["chrome_bypass_paywall_extension"]))
    driver = webdriver.Chrome(
        executable_path=os.path.join(config["chromedriver_path"], config["chrome_driver"]), options=options
    )
    time.sleep(5)
    while len(driver.window_handles) < int(config["max_web_driver_window"]):
        driver.execute_script('''window.open("http://www.google.com","_blank");''')
        time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    return driver


def get_firefox_driver_with_bypass_paywall(config: dict) -> WebDriver:
    options = firefox_options()
    options.binary_location = config["firefox_binary"]
    profile = webdriver.FirefoxProfile(config["firefox_profile"])
    driver = webdriver.Firefox(firefox_profile=profile, executable_path=config["firefox_driver"], options=options)
    return driver