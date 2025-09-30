from pages.hovers_page import HoversPage
from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)
EXCEPTED_USER1 = 'user1'
EXCEPTED_USER2 = 'user2'
EXCEPTED_USER3 = 'user3'
EXCEPTED_USER1_LINK = 'users/1'
EXCEPTED_USER2_LINK = 'users/2'
EXCEPTED_USER3_LINK = 'users/3'


def test_hovers(browser):
    page = HoversPage(browser.driver)
    browser.get(config.get('hovers_url'))
    page.wait_unique()
    page.hover_user(1)
    actual_user1_text = page.get_user_info(1)
    assert EXCEPTED_USER1 in actual_user1_text, f'EXCEPTED:  {EXCEPTED_USER1} not in Actual:{actual_user1_text}'
    page.open_user_link(1)
    actual_user_link = browser.get_url()
    assert EXCEPTED_USER1_LINK in actual_user_link, f'EXCEPTED: {EXCEPTED_USER1_LINK} Actual:{actual_user_link}'
    browser.back()
    page.wait_unique()
    page.hover_user(2)
    actual_user2_text = page.get_user_info(2)
    assert EXCEPTED_USER2 in actual_user2_text, f'EXCEPTED: {EXCEPTED_USER2} not in Actual:{actual_user2_text}'
    page.open_user_link(2)
    actual_user_link2 = browser.get_url()
    assert EXCEPTED_USER2_LINK in actual_user_link2, f'EXCEPTED: {EXCEPTED_USER2_LINK} Actual:{actual_user_link2}'
    browser.back()
    page.wait_unique()
    page.hover_user(3)
    actual_user3_text = page.get_user_info(3)
    assert EXCEPTED_USER3 in actual_user3_text, f'EXCEPTED: {EXCEPTED_USER3} not in Actual:{actual_user3_text}'
    page.open_user_link(3)
    actual_user_link3 = browser.get_url()
    assert EXCEPTED_USER3_LINK in actual_user_link3, f'EXCEPTED: {EXCEPTED_USER3_LINK} Actual:{actual_user_link3}'



