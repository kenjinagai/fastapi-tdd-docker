# project/tests/conftest.py


import os

import pytest
from starlette.testclient import TestClient

from app import main
from app.config import get_settings, Settings


def get_settings_override():
    return Settings(testing=1, database_url=os.environ.get("DATABASE_URL"))


@pytest.fixture(scope="module")
def test_app():
    # set up
# export      ENVIRONMENT=dev
#       export TESTING=0
#      export  DATABASE_URL=postgres://postgres:postgres@localhost:5432/web_dev        # new
#      export  DATABASE_TEST_URL=postgres://postgres:postgres@localhost:5432/web_test  # new


    main.app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(main.app) as test_client:

        # testing
        yield test_client

    # tear down
