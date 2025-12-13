import random

import pytest


@pytest.fixture(scope='session')
def api():
    return random.randint(210, 320)
