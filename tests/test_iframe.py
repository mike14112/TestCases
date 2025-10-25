from pages.frame_page import IFramePage
from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)
EXCEPT_UNIQUE_ELEM = 'FRAMES'.strip().lower()
EXCEPT_UNIQUE_ELEM_NESTED_FRAMES = 'NESTED FRAMES'.strip().lower()
EXCEPT_PARENT_FRAME = 'PARENT FRAME'.strip().lower()
EXCEPT_CHILD_FRAME = 'CHILD iFRAME'.strip().lower()
EXCEPT_UNIQUE_FRAME = 'FRAMES'.lower().strip()
EXCEPT_TEXT_FRAME = 'This is a sample page'.lower().strip()


def test_frames(browser):
    page = IFramePage(browser)
    browser.get(config.get('iframe_url'))
    actual_unique_elem = page.get_unique_elem()
    assert EXCEPT_UNIQUE_ELEM in actual_unique_elem, f'{EXCEPT_UNIQUE_ELEM} not in {actual_unique_elem}'
    page.click_btn_list_alerts()
    page.click_nested_frames()
    actual_nested_frames = page.get_unique_text_nested_frames()
    assert EXCEPT_UNIQUE_ELEM_NESTED_FRAMES in actual_nested_frames, (f'{EXCEPT_UNIQUE_ELEM_NESTED_FRAMES}'
                                                                      f' not in {actual_nested_frames}')
    browser.switch_frame('frame1')
    actual_parent_frame = page.get_text_parent_frame()
    assert EXCEPT_PARENT_FRAME in actual_parent_frame, f'{EXCEPT_PARENT_FRAME} not in {actual_parent_frame}'
    browser.switch_frame(0)
    actual_child_frame = page.get_text_child_frame()
    assert EXCEPT_CHILD_FRAME in actual_child_frame, f'{EXCEPT_CHILD_FRAME} not in {actual_child_frame}'
    browser.switch_to_default_content()
    page.click_btn_list_alerts()
    page.click_frame_menu()
    actual_frame_unique = page.get_text_unique_frame_page()
    assert EXCEPT_UNIQUE_FRAME in actual_frame_unique, f'{EXCEPT_UNIQUE_FRAME} not in {actual_frame_unique}'
    browser.switch_frame('frame1')
    actual_first_frame = page.get_text_frame()
    assert EXCEPT_TEXT_FRAME in actual_first_frame, f'{EXCEPT_TEXT_FRAME} not in {actual_first_frame}'
