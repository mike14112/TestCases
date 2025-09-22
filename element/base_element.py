from selenium.common import TimeoutException
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
        self.fast_wait = config.get('pull_frequency')

    def elem_text(self):
        try:
            Logger.info('Element text is {}'.format(self.description))
            return (WebDriverWait(self.driver, self.wait)).until(EC.presence_of_element_located(self.locator))
        except TimeoutException:
            Logger.error('Element text is not found')

    def elem_fast_wait(self):
        try:
            Logger.info('Element fast wait is {}'.format(self.description))
            return ((WebDriverWait(self.driver, self.wait, self.fast_wait))
                    .until(EC.presence_of_element_located(self.locator)))
        except TimeoutException:
            Logger.error('Element fast wait is not found')

    def elem_visible(self):
        try:
            Logger.info(f'self.description: {self.description}')
            return WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(self.locator))
        except TimeoutException:
            Logger.error(f'{self.description} is not found')

    def btn_click(self):
        try:
            Logger.info(f'self.description: {self.description}')
            return (WebDriverWait(self.driver, self.wait)
                    .until(EC.element_to_be_clickable(self.locator)).click())
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
