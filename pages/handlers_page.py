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
        self.page_name = 'handlers page'

        self.unique_elem = Label(self.browser, self.LOC_UNIQUE_ELEM, description='get url -> unique element')
        self.btn_new_window = Button(self.browser, self.LOC_BTN_ELEM,
                                     description='btn new window -> open new window')
        self.text_main_page = Label(self.browser, self.LOC_ELEM_TEXT, description='open page -> text main page')

    def get_text_elem(self):
        return self.text_main_page.get_text().lower().strip()

    def click_btn(self):
        self.btn_new_window.click()
