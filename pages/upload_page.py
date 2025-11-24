from elements.button import Button
from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class UploadPage(BasePage):
    LOC_UNIQUE_ELEM = "//*[@id='content']//h3"
    LOC_FILE_INPUT = 'file-upload'
    LOC_BTN_INPUT = 'file-submit'
    LOC_RESULT_TEXT = "//*[@id='content']//h3"
    LOC_NAME_FILE = "uploaded-files"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.page_name = 'upload file'

        self.unique_elem = Label(self.browser, self.LOC_UNIQUE_ELEM,
                                 'Open Page -> show unique file')
        self.load_file = WebElement(self.browser, self.LOC_FILE_INPUT,
                                    'load input -> file upload')
        self.btn_input = Button(self.browser, self.LOC_BTN_INPUT,
                                'click submit -> file upload')
        self.text_result = Label(self.browser, self.LOC_RESULT_TEXT,
                                 'Open new  Page -> show text result')
        self.file_name = Label(self.browser, self.LOC_NAME_FILE,
                               'Open new  Page -> file upload name text')

    def send_load_file(self, file_name):
        return self.load_file.send_keys(file_name)

    def click_btn_submit(self):
        self.btn_input.click()

    def get_text_result(self):
        return self.text_result.get_text()

    def get_file_name(self):
        return self.file_name.get_text()
