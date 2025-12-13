import random

import pytest


@pytest.fixture(scope="session")
def ui():
    return random.randint(2, 5)
