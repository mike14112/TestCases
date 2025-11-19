from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys

from elements.web_element import WebElement
from logger.logger import Logger


class Actions:
    def __init__(self, browser):
        self.driver = browser.driver

    def key_down(self, element: WebElement):
        try:
            return ActionChains(self.driver).key_down(Keys.ARROW_DOWN, element.wait_for_visibility()).perform()
        except TimeoutException:
            return Logger.error(f'Timeout exception occurred: not found element {element}')

    def key_right(self, element: WebElement):
        try:
            Logger.info('Move to element')
            return ActionChains(self.driver).send_keys_to_element(element.wait_for_visibility(),
                                                                  Keys.ARROW_RIGHT).perform()
        except TimeoutException:
            return Logger.error(f'Timeout exception occurred: not found element {element}')

    def click_context(self, element: WebElement):
        try:
            Logger.info('context_click')
            return ActionChains(self.driver).context_click(element.wait_for_visibility()).perform()
        except TimeoutException:
            return Logger.error(f'Timeout exception occurred: not found element {element}')

    def move_to_element(self, element: WebElement):
        try:
            return ActionChains(self.driver).move_to_element(element).perform()
        except TimeoutException:
            return Logger.error(f'Timeout exception occurred: not found element {element}')
