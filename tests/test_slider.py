from pages.slider_page import SliderPage
from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)
number = 1
number2 = 5


def test_slider(browser):
    page = SliderPage(browser)
    browser.get(config.get('slider_url'))
    page.wait_for_open()
    page.move_to_slider(number, number2)
