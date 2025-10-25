from pages.handlers_page import PageHandler
from utils.config_reader import ConfigReader
from utils.env import Env

EXCEPT_MAIN_PAGE = 'Opening a new window'.lower().strip()
EXCEPT_WINDOW = 'new window'.lower().strip()
config = ConfigReader(env=Env.DEV.value)


def test_handler(browser):
    page = PageHandler(browser.driver)
    browser.get(config.get('handlers_url'))
    actual = page.wait_elem_unique()
    assert EXCEPT_MAIN_PAGE in actual, f'EXCEPT {EXCEPT_MAIN_PAGE} is not in {actual}'
    page.click_btn()
    browser.switch_window(1)
    actual_window1 = browser.get_title_window().lower().strip()
    assert EXCEPT_WINDOW in actual_window1
    actual_elem_window = page.get_text_elem()
    assert EXCEPT_WINDOW in actual_elem_window, f'EXCEPT {EXCEPT_WINDOW} is not in {actual_elem_window}'
    browser.switch_window(0)
    assert EXCEPT_MAIN_PAGE in actual, f'EXCEPT {EXCEPT_MAIN_PAGE} is not in {actual}'
    page.click_btn()
    browser.switch_window(2)
    assert EXCEPT_WINDOW in actual_window1, f'EXCEPT {EXCEPT_WINDOW} is not in {actual_window1}'
    browser.switch_window(0)
    assert EXCEPT_MAIN_PAGE in actual, f'EXCEPT {EXCEPT_MAIN_PAGE} is not in {actual}'
    browser.switch_window(2)
    browser.close()
    browser.switch_window(1)
    browser.close()
    browser.switch_window(0)