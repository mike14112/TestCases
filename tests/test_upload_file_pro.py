import os
from pathlib import Path

import pytest

from pages.upload_file_pro_page import UploadPagePro
from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)
EXCEPT_RESULT = 'File Uploaded!'.lower().strip()
EXCEPT_FILE_NAME = 'f1'.lower().strip()
FILE_PATH = str(Path(__file__).resolve().parents[1] / "assets" / "f1.jpg")


@pytest.mark.skipif('DISPLAY' not in os.environ, reason="Нет графического дисплея (Docker)")
def test_upload_pro(browser):
    page = UploadPagePro(browser)
    browser.get(config.get('upload_url'))
    page.wait_for_open()
    page.file_load_set(FILE_PATH)
    actual_res = page.get_text_result()
    assert EXCEPT_RESULT in actual_res, f' Expected {EXCEPT_RESULT} is not {actual_res}'
    actual_file_name = page.get_file_name()
    assert EXCEPT_FILE_NAME in actual_file_name, f' Expected {EXCEPT_FILE_NAME} is not {actual_file_name}'
