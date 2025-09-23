from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from logger.logger import Logger
from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)
logger = Logger()


class BasePage:
    UNIQUE_LOQ = None

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.get('wait'))

    def get_url(self, url: str):
        Logger.info(f'opening url: {url}')
        self.driver.get(url)

    def switch_to_alert(self):
        try:
            Logger.info('switching to alert')
            alert = self.driver.switch_to.alert
            return alert
        except TimeoutException:
            Logger.error(f'alert not found')

    def accept_alert(self):
        try:
            logger.info(f'accepting alert')
            self.driver.switch_to.alert.accept()
        except TimeoutException:
            Logger.error(f'alert not found')

    def dismiss_alert(self):
        try:
            logger.info(f'dismiss alert')
            self.driver.switch_to.alert().dismiss()
        except TimeoutException:
            Logger.error(f'alert not found')
