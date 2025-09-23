from pages.page_alert import PageAlert
from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)
EXCEPT = 'Here are some examples of different JavaScript'.lower().strip()
EXCEPT_ALERT = 'I am a JS Alert'.lower().strip()
EXCEPT_ALERT_RESULT = 'You successfully clicked an alert'.lower().strip()
EXCEPT_CONFIRM = 'I am a JS Confirm'.lower().strip()
EXCEPT_CONFIRM_RESULT = 'You clicked: Ok'.lower().strip()


def test_alert(browser):
    driver = PageAlert(browser)
    driver.get_url(config.get('alert_basic'))
    actual = driver.wait_unique().text.lower().strip()
    assert EXCEPT in actual, f'EXCEPT{EXCEPT}  is not in actual {actual}'
    driver.click_btn_alert()
    actual_alert = driver.switch_to_alert().text.lower().strip()
    assert EXCEPT_ALERT in actual_alert, f'EXCEPT{EXCEPT_ALERT} is not in actual {actual_alert}'
    driver.switch_to_alert().accept()
    result_alert = driver.result_wait().text.lower().strip()
    assert EXCEPT_ALERT_RESULT in result_alert, f'EXCEPT{EXCEPT_ALERT_RESULT} is not in actual {result_alert}'
    driver.btn_confirm()
    actual_confirm = driver.switch_to_alert().text.lower().strip()
    assert EXCEPT_CONFIRM in actual_confirm, f'EXCEPT{EXCEPT_CONFIRM} is not in actual {actual_confirm}'
    driver.accept_alert()
    res_confirm = driver.result_wait().text.lower().strip()
    assert EXCEPT_CONFIRM_RESULT in res_confirm, f'EXCEPT{EXCEPT_CONFIRM_RESULT} is not in actual {res_confirm}'
