from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage


class PageHandler(BasePage):
    LOC_UNIQUE_ELEM = "//*[@id='content']//h3"
    LOC_BTN_ELEM = "//*[@id='content']//a"
    LOC_ELEM_TEXT = '//*[contains(@class, "example")]'

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

        self.unique_elem = Label(self.browser.driver, self.LOC_UNIQUE_ELEM, description='get url -> open page')
        self.btn_new_window = Button(self.browser.driver, self.LOC_BTN_ELEM, description='btn new window -> open new window')
        self.text_main_page = Label(self.browser.driver, self.LOC_ELEM_TEXT, description='open page -> text main page')

    def wait_elem_unique(self):
        return self.unique_elem.is_displayed().text.strip().lower()

    def get_text_elem(self):
        return self.text_main_page.is_displayed().text.strip().lower()


    def click_btn(self):
        return self.btn_new_window.btn_click()
