from pages.scroll_page import ScrollPage
from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)
NUMBER = 30


def test_scroll(browser):
    page = ScrollPage(browser)
    browser.get(config.get('scroll_url'))
    page.wait_for_open()
    count_paragraphs =  page.get_paragraph(NUMBER)
    assert len(count_paragraphs) == NUMBER, f'Expected :{NUMBER} not in {count_paragraphs} '