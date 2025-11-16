from elements.action_chains import Actions
from elements.web_element import WebElement
from pages.base_page import BasePage


class PageContext(BasePage):
    LOC_UNIQUE = "//h3[contains(text(), 'Context Menu')]"
    LOC_AREA = 'row'

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.page_name = 'Page context'
        self.actions = Actions(self.browser)

        self.unique_elem = WebElement(self.browser.driver, self.LOC_UNIQUE, description="open url -> unique element")
        self.area_elem = WebElement(self.browser.driver, self.LOC_AREA, description="area -> alert")

    def context_click(self):
        return self.actions.click_context(self.area_elem)
