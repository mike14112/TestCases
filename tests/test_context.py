from pages.page_context import PageContext
from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)

EXCEPT = 'Context Menu'.lower().strip()
EXCEPT_ALERT = 'You selected a context menu'.lower().strip()


def test_page_context(browser):
    page = PageContext(browser)
    browser.get(config.get('context_url'))
    actual = page.wait_unique().text.lower().strip()
    assert EXCEPT in actual, f'EXCEPT:{EXCEPT} not in {actual}'
    page.context_click()
