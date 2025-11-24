from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class ContextPage(BasePage):
    LOC_UNIQUE_ELEM = "//*[@id='content']//h3"
    LOC_AREA_ELEM = "hot-spot"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.page_name = 'context page'

        self.unique_elem = Label(self.browser, locator=self.LOC_UNIQUE_ELEM,
                                 description='open page -> opening')
        self.area_elem = WebElement(self.browser, locator=self.LOC_AREA_ELEM,
                                    description='area -> border area')

    def click_border(self):
        self.actions.click_context(self.area_elem)
