import pytest

from browser import Browser


@pytest.fixture(scope="function")
def browser(request):
    driver = Browser()
    yield driver
    driver.quit()
