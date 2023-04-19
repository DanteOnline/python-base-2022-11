"""
conftest
"""
from _pytest.fixtures import fixture
from flask.testing import FlaskClient

from main import app


@fixture
def client() -> FlaskClient:
    """
    FlaskClient
    :return:
    """
    with app.test_client() as test_client:
        yield test_client
