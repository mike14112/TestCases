from selenium.webdriver.common.by import By

from elements.base_element import BaseElement
from pages.base_page import BasePage


class PageContext(BasePage):
    LOC_UNIQUE = (By.XPATH, "//h3[contains(text(), 'Context Menu')]")
    LOC_AREA = (By.ID, 'row')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.unique_elem = BaseElement(self.driver, self.LOC_UNIQUE, description="Main page")
        self.area_elem = BaseElement(self.driver, self.LOC_AREA, description="area -> alert")

    def wait_unique(self):
        return self.unique_elem.elem_visible()

    def context_click(self):
        return self.area_elem.context_click()