from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from logger.logger import Logger
from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)


class BaseElement:
    def __init__(self, browser, locator, description):
        self.browser = browser
        self.locator = locator
        self.description = description
        self.wait = config.get('wait')
        self.pull = config.get('fast_pull_frequency')

        if isinstance(locator, str):
            if '/' in locator:
                self.locator = (By.XPATH, locator)
            else:
                self.locator = (By.ID, locator)
        else:
            self.locator = locator

    def wait_for_visibility(self):
        try:
            Logger.info(f'self.description: {self.description}')
            return WebDriverWait(self.browser.driver, self.wait, ).until(
                EC.visibility_of_element_located(self.locator))
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
            raise

    def wait_for_presence(self, pull=False):
        if pull:
            pull = self.pull
        try:
            Logger.info(f'self.description: {self.description}')
            return WebDriverWait(self.browser.driver, self.wait, poll_frequency=pull).until(
                EC.presence_of_element_located(self.locator))
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
            raise

    def get_text(self):
        element = self.wait_for_presence()
        Logger.info(f'self.description: {self.description}')
        return element.text

    def click(self):
        element = self.wait_for_visibility()
        Logger.info(f'self.description: {self.description}')
        element.click()

    def js_click(self):
        element = self.wait_for_presence()
        Logger.info(f'js click, self.description: {self.description} ')
        return self.browser.driver.execute_script('return arguments[0].click();', element)

    def scroll_to(self):
        Logger.info(f'self.description: {self.description}')
        return self.browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);",
                                                  self.wait_for_visibility())

    def send_keys(self, keys):
        element = self.wait_for_presence()
        Logger.info(f'self.description: {self.description}')
        return element.send_keys(keys)

    def get_attribute(self, attribute):
        element = self.wait_for_presence()
        Logger.info(f'self.description: {self.description}')
        return element.get_attribute(attribute)

    def get_property(self, attribute):
        element = self.wait_for_presence()
        Logger.info(f'self.description: {self.description}')
        return element.get_property(attribute)

    def is_exists(self):
        try:
            Logger.info(f'self.description: {self.description}')
            self.wait_for_presence()
            return True
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
            return False
