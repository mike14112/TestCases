from pages.context_page import ContextPage
from utils.config_reader import ConfigReader
from utils.env import Env
config = ConfigReader(env=Env.DEV.value)
EXCEPTED = 'Context Menu'.lower().strip('')
EXCEPTED_ALERT = 'You selected a context menu'.lower().strip('')

def test_context(browser):
    page = ContextPage(browser.driver)
    browser.get(config.get('context_url'))
    actual = page.wait_elem().text.lower().strip('')
    assert EXCEPTED in actual, f'Expected: {EXCEPTED}, not actual actual: {actual}'
    page.context_click()
    browser.switch_alert()
    actual_alert = browser.get_text_alert().lower().strip('')
    assert EXCEPTED_ALERT in actual_alert, f'Expected: {EXCEPTED_ALERT}, not actual actual: {actual_alert}'