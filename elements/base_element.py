from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
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

    def elem_fast_wait(self):
        try:
            Logger.info('Element fast wait is {}'.format(self.description))
            return WebDriverWait(self.driver, self.fast_wait).until(EC.presence_of_element_located(self.locator))
        except TimeoutException:
            Logger.error('Element fast wait is not found')

    def elem_visible(self):
        try:
            Logger.info(f'self.description: {self.description}')
            return WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(self.locator))
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
        raise

    def prefer_visible(self):
        try:
            Logger.info(f'self.description: {self.description}')
            return WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(self.locator))
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
        raise

    def btn_click(self):
        try:
            Logger.info(f'self.description: {self.description}')
            return WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(self.locator)).click()
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
        raise

    def js_click(self):
        try:
            Logger.info(f'self.description: {self.description}')
            element = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(self.locator))
            return self.driver.execute_script('return arguments[0].click();', element)
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
            raise

    def context_click(self):
        try:
            Logger.info(f'self.description: {self.description}')
            element = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(self.locator))
            return ActionChains(self.driver).context_click(element).perform()
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
            raise

    def move_element(self):
        try:
            Logger.info(f'self.description: {self.description}')
            element = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(self.locator))
            return (ActionChains(self.driver).click_and_hold(element)
                    .move_by_offset(yoffset=5, xoffset=0).release().perform())
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
            raise
