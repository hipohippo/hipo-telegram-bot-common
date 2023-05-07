import os
import time

from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver


def get_chrome_driver(config: dict) -> WebDriver:
    options = chrome_options()
    driver = webdriver.Chrome(
        executable_path=os.path.join(config["chromedriver_path"], config["chrome_driver"]), options=options
    )
    while len(driver.window_handles) < config["max_web_driver_window"]:
        driver.execute_script('''window.open("http://www.google.com","_blank");''')
        time.sleep(2)
    return driver
