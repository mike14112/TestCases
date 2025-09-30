from elements.label import Label
from pages.base_page import BasePage


class AuthPage(BasePage):
    UNIQ_ELEM = '//*[@id="content"]//p'

    def __init__(self, driver):
        super().__init__(driver)

        self.unique_elem = Label(driver=self.driver, locator=self.UNIQ_ELEM, description="Main page")

    def wait_unique(self):
        return self.unique_elem.elem_visible().text.lower().strip()
