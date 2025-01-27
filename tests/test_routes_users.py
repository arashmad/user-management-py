"""Test for /users routes."""

from fastapi.testclient import TestClient

from user_management_py.core import setting
from user_management_py.create_app import app

from .http_requests import do_post_request
from . import add_test_database, remove_test_database


SERVICE_NAMESPACE = setting.SERVICE_NAMESPACE


class TestRoutesUsers():
    """Test the users endpoint."""

    @classmethod
    def setup_class(cls):
        """
        Set up test fixtures.

        It is called once for the class.
        """
        add_test_database()

        cls.app = TestClient(app)
        cls.url = "/users"
        cls.test_uers = {
            "valid_account": {
                "email": "john.doe@user.domain",
                "password": "Adm!n1234"
            }
        }

    @classmethod
    def teardown_class(cls):
        """
        Tear down test fixtures.

        It is called once for the class.
        """
        remove_test_database()

    def setup_method(self):
        """
        Setup method.

        It is called for every method.
        """

    def teardown_method(self):
        """
        Tear down method.

        It is called for every method.
        """

    def test_api_users_create_new_accont(self):
        """Test [POST] /users for 200_OK."""
        status_code, json_data = \
            do_post_request(
                app=self.app,
                url=self.url,
                data=self.test_uers["valid_account"])

        assert status_code == 201
        assert "user" in json_data
        user_data = json_data["user"]
        assert user_data["email"] == self.test_uers["valid_account"]["email"]
        assert "user_id" in user_data
