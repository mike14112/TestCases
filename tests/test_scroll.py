from pages.scroll_page import ScrollPage
from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)


def test_scroll(browser):
    page = ScrollPage(browser)
    browser.get(config.get('scroll_url'))
    page.get_wait_unique()
    page.get_paragraph(30)

