from pages.upload_page import UploadPage
from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)
EXCEPT_RESULT = 'File Uploaded!'.lower().strip()
EXCEPT_FILE_NAME = 'f1'.lower().strip()
file_path = "assets/f1.jpg"


def test_upload(browser):
    page = UploadPage(browser)
    browser.get(config.get('upload_url'))
    page.wait_for_open()
    page.set_load_file('assets/f1.jpg')
    page.set_click_btn()
    actual_res = page.get_text_result()
    assert EXCEPT_RESULT in actual_res, f'Expected {EXCEPT_RESULT} is not {actual_res}'
    actual_file_name = page.get_file_name()
    assert EXCEPT_FILE_NAME in actual_file_name, f' Expected {EXCEPT_FILE_NAME} is not {actual_file_name}'
