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
    page = HoversPage(browser)
    browser.get(config.get('hovers_url'))
    page.wait_for_open()
    page.hover_user(1)
    actual_user1_text = page.get_user_info(1)
    assert actual_user1_text.endswith(EXCEPTED_USER1), f'Expected:  {EXCEPTED_USER1} not in Actual:{actual_user1_text}'
    page.open_user_link(1)
    actual_user_link = browser.get_url()
    assert actual_user_link.endswith(
        f'{EXCEPTED_USER1_LINK}'), f'Expected: {EXCEPTED_USER1_LINK} Actual:{actual_user_link}'
    browser.back()
    page.wait_for_open()
    page.hover_user(2)
    actual_user2_text = page.get_user_info(2)
    assert EXCEPTED_USER2 in actual_user2_text, f'Expected: {EXCEPTED_USER2} not in Actual:{actual_user2_text}'
    page.open_user_link(2)
    actual_user_link2 = browser.get_url()
    assert actual_user_link2.endswith(
        f'{EXCEPTED_USER2_LINK}'), f'Expected: {EXCEPTED_USER2_LINK} Actual:{actual_user_link2}'
    browser.back()
    page.wait_for_open()
    page.hover_user(3)
    actual_user3_text = page.get_user_info(3)
    assert EXCEPTED_USER3 in actual_user3_text, f'Expected: {EXCEPTED_USER3} not in Actual:{actual_user3_text}'
    page.open_user_link(3)
    actual_user_link3 = browser.get_url()
    assert actual_user_link3.endswith(
        f'{EXCEPTED_USER3_LINK}'), f'Expected: {EXCEPTED_USER3_LINK} Actual:{actual_user_link3}'
