import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)

@pytest.fixture(scope="function")
def browser():
   options = Options()
   options.add_argument(config.get('screen_size'))
   options.add_argument(config.get('maximized_screen'))
   driver = webdriver.Chrome(options=options)
   yield driver
   driver.quit()
