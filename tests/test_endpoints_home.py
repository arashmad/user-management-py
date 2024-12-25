#!/usr/bin/env python

"""Tests for `user_management_py` package."""

from fastapi.testclient import TestClient

from user_management_py.core import setting
from user_management_py.create_app import app

SERVICE_NAMESPACE = setting.SERVICE_NAMESPACE


class TestDataEndpointsHome():
    """Test the home endpoint."""

    @classmethod
    def setup_class(cls):
        """Set up test fixtures."""
        cls.app = TestClient(app)
        cls.endpoint_prefix = SERVICE_NAMESPACE

    @classmethod
    def teardown_class(cls):
        """Tear down test fixtures."""
        print("teardown_class called once for the class")

    @classmethod
    def setup_method(cls):
        """Setup method."""
        print("setup_method called for every method")

    @classmethod
    def teardown_method(cls):
        """Tear down method."""
        print("teardown_method called for every method")

    def test_api_home_200(self):
        """Test the home endpoint."""
        response = self.app.get(f"{self.endpoint_prefix}/")
        assert response.status_code == 200

    def test_api_home_404_url_not_found(self):
        """Test the home endpoint with a non existing url."""
        response = self.app.get(f"{self.endpoint_prefix}/NotFound")
        assert response.status_code == 404
