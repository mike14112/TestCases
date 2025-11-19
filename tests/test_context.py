from pages.context_page import ContextPage
from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)

EXCEPT_ALERT = 'You selected a context menu'.lower().strip()


def test_page_context(browser):
    page = ContextPage(browser)
    browser.get(config.get('context_url'))
    page.wait_for_open()
    page.click_border()
    actual_alert = browser.get_text_alert().lower().strip()
    assert EXCEPT_ALERT in actual_alert, f'Expected :{EXCEPT_ALERT} not in {actual_alert}'
