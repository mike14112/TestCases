from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)


class BrowserFactory:
    @staticmethod
    def get_browser_instance():
        options = Options()
        options.add_argument(config.get("screen_size"))
        options.add_argument(config.get("headless"))
        options.add_argument(config.get("no_sandbox"))
        return webdriver.Chrome(options=options)
