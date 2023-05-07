from typing import List, Optional, Union

from selenium.webdriver.chrome.webdriver import WebDriver

from hipo_telegram_bot_common.bot_config.bot_config import BotConfig


class WebDriverBotConfig(BotConfig):
    ## todo make it interface/multiple implements
    def __init__(
            self,
            heart_beat_chat: Union[int, str],
            error_notify_chat: Union[int, str],
            white_list_id: Optional[List[int]],
            bot_name: str,
            web_driver: WebDriver
    ):
        super().__init__(heart_beat_chat, error_notify_chat, white_list_id, bot_name)
        self._web_driver = web_driver

    @property
    def web_driver(self) -> WebDriver:
        return self._web_driver

    @web_driver.setter
    def web_driver(self, value):
        self._web_driver = value

