# project/tests/conftest.py


import os

import pytest
from starlette.testclient import TestClient

from app.main import create_application  # updated
from app.config import get_settings, Settings
from tortoise.contrib.fastapi import register_tortoise


def get_settings_override():
    return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))


@pytest.fixture(scope="module")
def test_app():
    # set up
# export ENVIRONMENT=dev
# export TESTING=0
# export DATABASE_URL=postgres://postgres:postgres@localhost:5432/web_dev
# export DATABASE_TEST_URL=postgres://postgres:postgres@localhost:5432/web_test
    os.environ["ENVIRONMENT"] = "dev"
    os.environ["TESTING"] = "0"
    os.environ["DATABASE_URL"] = "postgres://postgres:postgres@localhost:5432/web_dev"
    os.environ["DATABASE_TEST_URL"] = "postgres://postgres:postgres@localhost:5432/web_test"



    app = create_application()  # new
    app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(app) as test_client:

        # testing
        yield test_client

    # tear down


# new
@pytest.fixture(scope="module")
def test_app_with_db():
    # set up
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_TEST_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    with TestClient(app) as test_client:

        # testing
        yield test_client

    # tear down