from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from logger.logger import Logger
from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)


class BaseElement:
    def __init__(self, driver, locator, description):
        self.driver = driver
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

    def wait_for_presence(self):
        try:
            Logger.info('Element fast wait is {}'.format(self.description))
            return WebDriverWait(self.driver, self.fast_wait).until(EC.presence_of_element_located(self.locator))
        except TimeoutException:
            Logger.error('Element fast wait is not found')
            raise

    def visibility_of_elem(self):
        try:
            Logger.info(f'self.description: {self.description}')
            return WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(self.locator))
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
            raise

    def presence_of_element(self):
        try:
            Logger.info(f'self.description: {self.description}')
            return WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(self.locator))
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
            raise

    def get_text(self):
        try:
            Logger.info(f'self.description: {self.description}')
            return WebDriverWait(self.driver, self.fast_wait).until(
                EC.presence_of_element_located(self.locator)).text.strip().lower()
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
            raise

    def click_elem(self):
        try:
            Logger.info(f'self.description: {self.description}')
            return WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(self.locator)).click()
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
            raise

    def js_click(self):
        try:
            Logger.info(f'self.description: {self.description}')
            element = WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(self.locator))
            return self.driver.execute_script('return arguments[0].click();', element)
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
            raise

    def get_attribute(self, attribute):
        try:
            Logger.info(f'self.description: {self.description}')
            return WebDriverWait(self.driver, self.wait).until(
                EC.presence_of_element_located(self.locator)).get_attribute(attribute)
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
