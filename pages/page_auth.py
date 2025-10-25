from elements.label import Label
from pages.base_page import BasePage


class AuthPage(BasePage):
    LOC_UNIQUE_ELEM = '//*[@id="content"]//p'

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

        self.unique_elem = Label(driver=self.browser.driver, locator=self.LOC_UNIQUE_ELEM, description="Main page")

    def wait_unique(self):
        return self.unique_elem.elem_visible().text.lower().strip()
