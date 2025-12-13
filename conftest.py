import random

import pytest


@pytest.fixture(scope="session")
def base_url():
    return random.randint(2, 5)
