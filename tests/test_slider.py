from pages.slider_page import SliderPage
from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)


def test_slider(browser):
    page = SliderPage(browser)
    browser.get(config.get('slider_url'))
    page.wait_for_open()
    number = page.get_min_step()
    number2 = page.get_max_step()
    page.move_to_slider(number, number2)
