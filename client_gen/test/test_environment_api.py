# coding: utf-8

"""
    home-iot-api

    The API for the EatBacon IOT project  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.environment_api import EnvironmentApi  # noqa: E501
from swagger_client.rest import ApiException


class TestEnvironmentApi(unittest.TestCase):
    """EnvironmentApi unit test stubs"""

    def setUp(self):
        self.api = EnvironmentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_forecast(self):
        """Test case for get_forecast

        """
        pass

    def test_get_heater_state(self):
        """Test case for get_heater_state

        """
        pass

    def test_get_zone_temperature(self):
        """Test case for get_zone_temperature

        """
        pass

    def test_set_heater_state(self):
        """Test case for set_heater_state

        """
        pass

    def test_temperature_summary(self):
        """Test case for temperature_summary

        """
        pass


if __name__ == '__main__':
    unittest.main()
