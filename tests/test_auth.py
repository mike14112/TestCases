import pytest

from pages.page_auth import AuthPage
from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)
EXCEPT = 'Congratulations! you must have the proper credentials.'.lower().strip()


@pytest.mark.parametrize('login, password', [
    ['admin', 'admin'],
])
def test_auth(browser, login, password):
    driver = AuthPage(browser)
    link = config.get('basic_auth')
    driver.get_url(f'https://{login}:{password}@{link}')
    actual = driver.wait_unique().text.lower().strip()
    assert EXCEPT in actual, f'expected: {EXCEPT} to be in {actual}'
