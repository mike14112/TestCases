from elements.base_element import BaseElement
from pages.base_page import BasePage


class PageContext(BasePage):
    LOC_UNIQUE = "//h3[contains(text(), 'Context Menu')]"
    LOC_AREA = 'row'

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.page_name = 'Page context'

        self.unique_elem = BaseElement(self.browser.driver, self.LOC_UNIQUE, description="Main page")
        self.area_elem = BaseElement(self.browser.driver, self.LOC_AREA, description="area -> alert")

    def context_click(self):
        return self.area_elem.context_click()
