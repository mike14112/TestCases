import pytest

from pages.page_auth  import AuthPage
from utils.config_reader import ConfigReader
from utils.env import Env
config = ConfigReader(env=Env.DEV.value)
EXCEPT = 'Congratulations! you must have the proper credentials.'.lower().strip()

@pytest.mark.parametrize('login, password', [
    ['admin', 'admin'],
])
def test_auth(browser, login, password):
    page = AuthPage(browser)
    link = config.get('basic_auth')
    browser.get(f'https://{login}:{password}@{link}')
    actual  =  page.wait_unique()
    assert EXCEPT in actual, f'expected: {EXCEPT} to be in {actual}'
