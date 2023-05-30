import time
from typing import List

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def deepl_setup(driver: WebDriver, page_index: int, target_lang: str):
    driver.switch_to.window(driver.window_handles[page_index])
    driver.get("https://www.deepl.com/en/translator#en/zh")
    element = driver.find_element(By.XPATH, '//div[@role="textbox"]')
    target_lang_menu_element = driver.find_element(
        By.XPATH, '//div[@class="lmt__language_select lmt__language_select--target"]'
    )
    target_lang_menu_element.click()
    target_lang = "translator-lang-option-zh"
    target_lang_button_element = driver.find_element(By.XPATH, f'//button[@data-testid="{target_lang}"]')
    target_lang_button_element.click()


def deepl_translate(driver: WebDriver, page_index:int, throttle: int, original_text: str):
    driver.switch_to.window(driver.window_handles[page_index])
    element = driver.find_element(By.XPATH, '//div[@role="textbox"]')
    element.clear()
    element.send_keys(original_text)
    target_lang_text = driver.find_element(
        By.XPATH, '//section[@class="lmt__side_container lmt__side_container--target"]//div[@role="textbox"]'
    )
    time.sleep(throttle)
    translated = target_lang_text.text
    return translated


def deepl_bulk_translate(driver: WebDriver, page_index:int, throttle: int, paragraphs: List[str]):
    translated = []
    for paragraph in paragraphs:
        translated.append(deepl_translate(driver, page_index, throttle, paragraph))
    return translated
