from utils.config_reader import ConfigReader
from utils.env import Env
from pages.dynamic_page import DynamicPage

config_reader = ConfigReader(env=Env.DEV.value)

def test_dynamic(browser):
    page = DynamicPage(browser)
    browser.get(config_reader.get('dynamic_url'))
    page.get_unique_element()
    page.match_img()


