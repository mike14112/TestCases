from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait

from elements.base_element import BaseElement
from logger.logger import Logger


class Actions(BaseElement):
    def key_down(self):
        try:
            Logger.info(f'self.description: {self.description}')
            element = WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(self.locator))
            return ActionChains(self.driver).key_down(Keys.ARROW_DOWN, element).perform()
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
            raise

    def move_element(self):
        try:
            Logger.info(f'self.description: {self.description}')
            element = WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(self.locator))
            return (ActionChains(self.driver).click_and_hold(element)
                    .move_by_offset(yoffset=5, xoffset=0).release().perform())
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
            raise

    def context_click(self):
        try:
            Logger.info(f'self.description: {self.description}')
            element = WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(self.locator))
            return ActionChains(self.driver).context_click(element).perform()
        except TimeoutException:
            Logger.error(f'{self.description} is not found')
            raise
