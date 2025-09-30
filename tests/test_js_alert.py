from pages.page_alert import PageAlert
from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)
EXCEPT = 'javascript alerts'.lower().strip()
EXCEPT_ALERT = 'I am a JS Alert'.lower().strip()
EXCEPT_ALERT_RESULT = 'You successfully clicked an alert'.lower().strip()
EXCEPT_CONFIRM = 'I am a JS Confirm'.lower().strip()
EXCEPT_CONFIRM_RESULT = 'You clicked: Ok'.lower().strip()


def test_alert(browser):
    pages = PageAlert(browser.driver)
    browser.get(config.get('alert_basic'))
    actual = pages.wait_unique()
    assert EXCEPT in actual, f'EXCEPT{EXCEPT}  is not in actual {actual}'
    pages.click_btn_alert()
    actual_alert = browser.get_text_alert().lower().strip()
    assert EXCEPT_ALERT in actual_alert, f'EXCEPT{EXCEPT_ALERT} is not in actual {actual_alert}'
    browser.confirm_alert()
    result_alert = pages.result_wait()
    assert EXCEPT_ALERT_RESULT in result_alert, f'EXCEPT{EXCEPT_ALERT_RESULT} is not in actual {result_alert}'
    pages.btn_confirm()
    actual_confirm = browser.get_text_alert().lower().strip()
    assert EXCEPT_CONFIRM in actual_confirm, f'EXCEPT{EXCEPT_CONFIRM} is not in actual {actual_confirm}'
    browser.confirm_alert()
    res_confirm = pages.result_wait()
    assert EXCEPT_CONFIRM_RESULT in res_confirm, f'EXCEPT{EXCEPT_CONFIRM_RESULT} is not in actual {res_confirm}'
