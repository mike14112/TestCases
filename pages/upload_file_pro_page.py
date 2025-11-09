import utils.pyautogui as pyautogui
from elements.button import Button
from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class UploadPagePro(BasePage):
    LOC_UNIQUE_ELEM = "//*[@id='content']//h3"
    LOC_FILE_INPUT = 'file-upload'
    LOC_BTN_INPUT = 'file-submit'
    LOC_RESULT_TEXT = "//*[@id='content']//h3"
    LOC_NAME_FILE = "uploaded-files"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.page_name ='upload file pro'

        self.unique_elem = Label(self.browser.driver, self.LOC_UNIQUE_ELEM,
                                 'Open Page -> show unique file')
        self.load_file = WebElement(self.browser.driver, self.LOC_FILE_INPUT,
                                    'load input -> file upload')
        self.btn_input = Button(self.browser.driver, self.LOC_BTN_INPUT,
                                'click submit -> file upload')
        self.text_result = Label(self.browser.driver, self.LOC_RESULT_TEXT,
                                 'Open new  Page -> show text result')
        self.file_name = Label(self.browser.driver, self.LOC_NAME_FILE,
                               'Open new  Page -> file upload name text')

    def get_unique_elem(self):
        return self.unique_elem.is_displayed()

    def set_load_file(self):
        return pyautogui.PyAutoGui.upload_file('/assets/f1.jpg')

    def set_click_btn(self):
        return self.btn_input.is_displayed().click()

    def get_text_result(self):
        return self.text_result.elem_fast_wait().text.lower().strip()

    def get_file_name(self):
        return self.file_name.elem_fast_wait().text.lower().strip()
