from selenium.webdriver.common.by import By

from elements.base_element import BaseElement
from pages.base_page import BasePage


class PageContext(BasePage):
    LOC_UNIQUE = (By.XPATH, "//h3[contains(text(), 'Context Menu')]")
    LOC_AREA = (By.ID, 'row')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

        self.unique_elem = BaseElement(self.browser.driver, self.LOC_UNIQUE, description="Main page")
        self.area_elem = BaseElement(self.browser.driver, self.LOC_AREA, description="area -> alert")

    def wait_unique(self):
        return self.unique_elem.is_displayed()

    def context_click(self):
        return self.area_elem.context_click()