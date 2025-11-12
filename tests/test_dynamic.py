from utils.config_reader import ConfigReader
from utils.env import Env
from pages.dynamic_page import DynamicPage

config_reader = ConfigReader(env=Env.DEV.value)

def test_dynamic(browser):
    page = DynamicPage(browser)
    browser.get(config_reader.get('dynamic_url'))
    page.get_wait_unique()
    imgs = page.get_all_src()
    for i, img in enumerate(imgs):
        if img[i] != img[i+1]:
            browser.refresh()
        else:
            break




