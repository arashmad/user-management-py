"""Test for / routes."""

from fastapi.testclient import TestClient

from user_management_py.create_app import app


class TestHealth():
    """Test the home endpoint."""

    @classmethod
    def setup_class(cls):
        """
        Set up test fixtures.

        It is called once for the class.
        """
        cls.app = TestClient(app)
        cls.url = "/"

    @classmethod
    def teardown_class(cls):
        """
        Tear down test fixtures.

        It is called once for the class.
        """

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

    def test_api_home_200(self):
        """Test the home endpoint."""
        response = self.app.get(self.url)
        assert response.status_code == 200

    def test_api_home_404_url_not_found(self):
        """Test the home endpoint with a non existing url."""
        response = self.app.get(f"{self.url}NotFound")
        assert response.status_code == 404
