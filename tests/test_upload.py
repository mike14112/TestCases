from pathlib import Path

from pages.upload_page import UploadPage
from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)
EXCEPT_RESULT = 'File Uploaded!'.lower().strip()
EXCEPT_FILE_NAME = 'f1'.lower().strip()
FILE_PATH = str(Path(__file__).resolve().parents[1] / "assets" / "f1.jpg")


def test_upload(browser):
    page = UploadPage(browser)
    browser.get(config.get('upload_url'))
    page.wait_for_open()
    page.send_load_file(FILE_PATH)
    page.click_btn_submit()
    actual_res = page.get_text_result()
    assert EXCEPT_RESULT in actual_res, f'Expected {EXCEPT_RESULT} is not {actual_res}'
    actual_file_name = page.get_file_name()
    assert EXCEPT_FILE_NAME in actual_file_name, f' Expected {EXCEPT_FILE_NAME} is not {actual_file_name}'
