from pages.context_page import ContextPage
from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)

EXCEPT_ALERT = 'You selected a context menu'.lower().strip()


def test_page_context(browser):
    page = ContextPage(browser)
    browser.get(config.get('context_url'))
    page.get_wait_unique()
    page.click_context()
    actual_alert = browser.get_text_alert().lower().strip()
    assert EXCEPT_ALERT in actual_alert, f'EXCEPT_ALERT:{EXCEPT_ALERT} not in {actual_alert}'

