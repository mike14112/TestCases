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
        self.fast_wait = config.get('fast_pull_frequency')

        if isinstance(locator, str):
            if '/' in locator:
                self.locator = (By.XPATH, locator)
            else:
                self.locator = (By.ID, locator)
        else:
            self.locator = locator

    def wait_for_presence_fast_pull(self):
        try:
            Logger.info('Element fast wait is {}'.format(self.description))
            return WebDriverWait(self.browser.driver, self.fast_wait).until(
                EC.presence_of_element_located(self.locator))
        except TimeoutException:
            Logger.error('Element fast wait is not found')
            raise

    def wait_for_visibility(self):
        try:
            Logger.info(f'self.description: {self.description}')
            return WebDriverWait(self.browser.driver, self.wait).until(EC.visibility_of_element_located(self.locator))
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
            raise

    def presence_of_element(self):
        try:
            Logger.info(f'self.description: {self.description}')
            return WebDriverWait(self.browser.driver, self.wait).until(EC.presence_of_element_located(self.locator))
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
            raise

    def get_text(self):
        try:
            element = self.presence_of_element()
            Logger.info(f'self.description: {self.description}')
            return element.text
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
            raise

    def click(self):
        try:
            Logger.info(f'self.description: {self.description}')
            return WebDriverWait(self.browser.driver, self.wait).until(EC.element_to_be_clickable(self.locator)).click()
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
            raise

    def js_click(self):
        try:

            element = self.presence_of_element()
            Logger.info(f'js click, self.description: {self.description} ')
            return self.browser.driver.execute_script('return arguments[0].click();', element)
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
            raise

    def scroll_to_in_to(self):
        try:
            element = self.presence_of_element()
            Logger.info(f'self.description: {self.description}')
            return self.browser.driver.execute_script('return arguments[0].scrollIntoView();', element)
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
            raise

    def get_attribute(self, attribute):

        try:
            element = self.presence_of_element()
            Logger.info(f'self.description: {self.description}')
            element.get_attribute(attribute)

        except TimeoutException:
            Logger.error(f'{self.description} is not found')
            raise

    def get_property(self, attribute):
        try:
            element = self.presence_of_element()
            Logger.info(f'self.description: {self.description}')
            return element.get_attribute(attribute)

        except TimeoutException:
            Logger.error(f'{self.description} is not found')
            raise

    def is_exists(self):
        try:
            Logger.info(f'self.description: {self.description}')
            self.presence_of_element()
            return True
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
            return False
