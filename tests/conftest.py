import pytest
from browser import Browser

@pytest.fixture(scope="function")
def browser():
   driver = Browser()
   yield driver
   driver.quit()
