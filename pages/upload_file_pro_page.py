import utils.pyautogui as pyauto
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
        self.page_name = 'upload file pro'

        self.unique_elem = Label(self.browser, self.LOC_UNIQUE_ELEM,
                                 'wait for Open Page -> show unique file')
        self.load_file = WebElement(self.browser, self.LOC_FILE_INPUT,
                                    'load input -> file upload')
        self.btn_input = Button(self.browser, self.LOC_BTN_INPUT,
                                'click submit -> file upload')
        self.text_result = Label(self.browser, self.LOC_RESULT_TEXT,
                                 'wait for open  Page -> show text result')
        self.file_name = Label(self.browser, self.LOC_NAME_FILE,
                               'wait for open new  Page -> file upload name text')

    def file_load_set(self, file_path):
        self.load_file.click()
        pyauto.PyAutoGui.upload_file(file_path)
        self.btn_input.click()

    def get_text_result(self):
        return self.text_result.get_text()

    def get_file_name(self):
        return self.file_name.get_text()
