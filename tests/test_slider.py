from pages.slider_page import SliderPage
from utils.config_reader import ConfigReader
from utils.env import Env
config = ConfigReader(env=Env.DEV.value)

def test_slider(browser):
    page = SliderPage(browser.driver)
    browser.get(config.get('slider_url'))
    page.wait_unique()
    page.move_to_slider()

