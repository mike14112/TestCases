from pages.scroll_page import ScrollPage
from utils.config_reader import ConfigReader
from utils.env import  Env

config = ConfigReader(env=Env.DEV.value)

def test_scroll(browser):
    page = ScrollPage(browser.driver)
    browser.get(config.get('scroll_url'))
    page.get_unique_elem()
    page.count_paragraph()
