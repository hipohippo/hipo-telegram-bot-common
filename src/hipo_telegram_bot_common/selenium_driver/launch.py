import os
import time
from typing import Optional

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options as firefox_options


def tchrome():
    options = chrome_options()
    #   options.add_extension(os.path.join(config["chromedriver_path"], config["chrome_bypass_paywall_extension"]))
    options.add_experimental_option("debuggerAddress", f"127.0.0.1:19287")
    # options.add_argument("--user-data-dir=/home/hipo/bots/selenium-driver/chrome-profile")
    # options.add_argument("--headless=new")
    # options.add_argument("--no-sandbox")
    # options.binary_location="/opt/google/chrome/google-chrome"
    epath = "/home/hipo/botrun/selenium-driver/chromedriver-linux64/chromedriver"
    # driver = webdriver.Chrome(executable_path=epath, options=options)
    driver = webdriver.Chrome(executable_path=epath)
    driver.set_page_load_timeout(5)
    driver.get("http://www.baidu.com")
    driver.get(
        "http://www.sina.com.cn",
    )
    time.sleep(5)


def get_chrome_driver(config: dict, load_extension: False, given_port: Optional[int]) -> WebDriver:
    options = chrome_options()
    if load_extension:
        options.add_argument(f'load-extension={config["chrome_bypass_paywall_extension"]}')
    if given_port:
        pass
        # options.add_experimental_option("debuggerAddress", f"127.0.0.1:{given_port}")
        # options.add_argument("user-data-dir=/home/hipo/bots/selenium-driver/chrome-profile")
        # options.add_argument("--headless=")
        # options.add_argument("--no-sandbox")
    print(os.path.join(config["chromedriver_path"], config["chrome_driver"]))
    driver = webdriver.Chrome(
        executable_path=os.path.join(config["chromedriver_path"], config["chrome_driver"]), options=options
    )
    # driver.switch_to.window(driver.window_handles[int(config["designated_window_handle"])])
    return driver


def get_firefox_driver_with_bypass_paywall(config: dict) -> WebDriver:
    options = firefox_options()
    options.binary_location = config["firefox_binary"]
    profile = webdriver.FirefoxProfile(config["firefox_profile"])
    driver = webdriver.Firefox(firefox_profile=profile, executable_path=config["firefox_driver"], options=options)
    return driver
