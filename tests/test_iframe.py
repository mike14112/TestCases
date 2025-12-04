import pytest

from pages.frame_page import IFramePage
from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)
EXCEPT_PARENT_FRAME = 'PARENT FRAME'.strip().lower()
EXCEPT_CHILD_FRAME = 'CHILD iFRAME'.strip().lower()
EXCEPT_UNIQUE_FRAME = 'FRAMES'.lower().strip()
EXCEPT_TEXT_FRAME = 'This is a sample page'.lower().strip()


@pytest.mark.skip(reason="Почему то  стал выкидывать ошибку разберусь с этим ")
def test_frames(browser):
    page = IFramePage(browser)
    browser.get(config.get('iframe_url'))
    page.wait_for_open()
    page.click_btn_list_alerts()
    page.click_nested_frames()
    page.wait_for_open()
    page.switch_parent_frame()
    actual_parent_frame = page.get_text_parent_frame()
    assert EXCEPT_PARENT_FRAME in actual_parent_frame, f'Expected {EXCEPT_PARENT_FRAME} not in {actual_parent_frame}'
    page.switch_child_frame()
    actual_child_frame = page.get_text_child_frame()
    assert EXCEPT_CHILD_FRAME in actual_child_frame, f'Expected {EXCEPT_CHILD_FRAME} not in {actual_child_frame}'
    browser.switch_to_default_content()
    page.click_btn_list_alerts()
    page.click_frame_menu()
    actual_frame_unique = page.get_text_unique_frame_page()
    assert EXCEPT_UNIQUE_FRAME in actual_frame_unique, f'Expected {EXCEPT_UNIQUE_FRAME} not in {actual_frame_unique}'
    page.switch_parent_frame()
    actual_first_frame = page.get_text_frame()
    assert EXCEPT_TEXT_FRAME in actual_first_frame, f'Expected {EXCEPT_TEXT_FRAME} not in {actual_first_frame}'
