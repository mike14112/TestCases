from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage


class PageHandler(BasePage):
    LOQ_UNIQUE_ELEM = "//*[@id='content']//h3"
    LOQ_BTN_ELEM = "//*[@id='content']//a"
    LOQ_ELEM_TEXT = '//*[contains(@class, "example")]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.unique_elem = Label(self.driver, self.LOQ_UNIQUE_ELEM, description='get url -> open page')
        self.btn_new_window = Button(self.driver, self.LOQ_BTN_ELEM, description='btn new window -> open new window')
        self.text_main_page = Label(self.driver, self.LOQ_ELEM_TEXT, description='open page -> text main page')

    def wait_elem_unique(self):
        return self.unique_elem.get_text().strip().lower()

    def get_text_elem(self):
        return self.text_main_page.get_text().strip().lower()


    def click_btn(self):
        return self.btn_new_window.btn_click()
