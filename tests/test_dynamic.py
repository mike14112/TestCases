from pages.dynamic_page import DynamicPage
from utils.config_reader import ConfigReader
from utils.env import Env

config_reader = ConfigReader(env=Env.DEV.value)


def test_dynamic(browser):
    page = DynamicPage(browser)
    browser.get(config_reader.get('dynamic_url'))
    page.wait_for_open()
    imgs = page.get_all_src()
    for i in range(len(imgs) - 1):
        if imgs[i] != imgs[i + 1]:
            browser.refresh()
        else:
            break
