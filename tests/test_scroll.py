import random

from pages.scroll_page import ScrollPage
from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)
number = 30

def test_scroll(browser):
    page = ScrollPage(browser)
    browser.get(config.get('scroll_url'))
    page.wait_for_open()
    page.get_paragraph(number)

