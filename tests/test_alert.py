from pages.page_alert import PageAlert
from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)

EXCEPT_ALERT_RESULT = 'You successfully clicked an alert'.lower().strip()
EXCEPT_CONFIRM = 'I am a JS Confirm'.lower().strip()
EXCEPT_CONFIRM_RESULT = 'You clicked: Ok'.lower().strip()


def test_alert(browser):
    page = PageAlert(browser)
    browser.get(config.get('alert_basic'))
    page.wait_for_open()
    page.click_btn_alert()
    browser.switch_alert()
    browser.confirm_alert()
    result_alert = page.get_result_wait()
    assert EXCEPT_ALERT_RESULT in result_alert, f'Expected{EXCEPT_ALERT_RESULT} is not in actual {result_alert}'
    page.btn_confirm()
    actual_confirm = browser.get_text_alert().lower().strip()
    assert EXCEPT_CONFIRM in actual_confirm, f'Expected{EXCEPT_CONFIRM} is not in actual {actual_confirm}'
    browser.confirm_alert()
    res_confirm = page.get_result_wait()
    assert EXCEPT_CONFIRM_RESULT in res_confirm, f'Expected{EXCEPT_CONFIRM_RESULT} is not in actual {res_confirm}'
