import random

import pytest


@pytest.fixture(scope="session")
def api_load():
    return random.randint(50, 100)
