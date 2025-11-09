from elements.action_chains import Actions
from elements.label import Label
from pages.base_page import BasePage


class ContextPage(BasePage):
    LOC_UNIQUE_ELEM = "//*[@id='content']//h3"
    lOC_AREA_ELEM = "hot-spot"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.page_name = 'context page'

        self.unique_elem = Label(driver=self.browser.driver, locator=self.LOC_UNIQUE_ELEM,
                                 description='open page -> opening')
        self.area = Actions(driver=self.browser.driver, locator=self.lOC_AREA_ELEM, description='button -> alert')

    def click_context(self):
        return self.area.context_click()
