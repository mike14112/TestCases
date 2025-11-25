from elements.label import Label
from pages.base_page import BasePage


class AuthPage(BasePage):
    LOC_UNIQUE_ELEM = '//*[@id="content"]//p'

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.page_name = 'Auth Page'

        self.unique_elem = Label(self.browser, locator=self.LOC_UNIQUE_ELEM,
                                 description="wait for open  -> unique element")
