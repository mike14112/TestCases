from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage


class ContextPage(BasePage):
    LOC_UNIQUE_ELEM = "//*[@id='content']//h3"
    lOC_AREA_ELEM = "hot-spot"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

        self.unique_elem = Label(driver=self.browser.driver, locator=self.LOC_UNIQUE_ELEM, description='open page -> opening')
        self.area = Button(driver=self.browser.driver, locator=self.lOC_AREA_ELEM, description='button -> alert')

    def wait_unique(self):
        return self.unique_elem.is_displayed().text.lower().strip(' ')

    def context_click(self):
        return self.area.context_click()
