from pages.upload_page import UploadPage
from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)
EXCEPT_RESULT = 'File Uploaded!'.lower().strip()
EXCEPT_FILE_NAME = 'f1'.lower().strip()

def test_upload(browser):
    page = UploadPage(browser.driver)
    browser.get(config.get('upload_url'))
    page.get_unique_elem()
    page.set_load_file()
    page.set_click_btn()
    actual_res =  page.get_text_result()
    assert EXCEPT_RESULT in actual_res, f'{EXCEPT_RESULT} is not {actual_res}'
    actual_file_name = page.get_file_name()
    assert EXCEPT_FILE_NAME in actual_file_name, f'{EXCEPT_FILE_NAME} is not {actual_file_name}'
