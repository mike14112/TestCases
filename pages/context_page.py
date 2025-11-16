from elements.action_chains import Actions
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
        self.actions = Actions(self.browser)

        self.unique_elem = Label(driver=self.browser.driver, locator=self.LOC_UNIQUE_ELEM,
                                 description='open page -> opening')
        self.area_elem = WebElement(driver=self.browser.driver, locator=self.LOC_AREA_ELEM,
                               description='area -> context  area')

    def click_context(self):
        return self.actions.click_context(self.area_elem)
