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
from swagger_client.api.z_wave_api import ZWaveApi  # noqa: E501
from swagger_client.rest import ApiException


class TestZWaveApi(unittest.TestCase):
    """ZWaveApi unit test stubs"""

    def setUp(self):
        self.api = ZWaveApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_lighting_summary(self):
        """Test case for get_lighting_summary

        """
        pass

    def test_get_switch_state(self):
        """Test case for get_switch_state

        """
        pass

    def test_set_dimmer(self):
        """Test case for set_dimmer

        """
        pass

    def test_set_dimmer_timer(self):
        """Test case for set_dimmer_timer

        """
        pass

    def test_set_switch(self):
        """Test case for set_switch

        """
        pass

    def test_set_switch_timer(self):
        """Test case for set_switch_timer

        """
        pass


if __name__ == '__main__':
    unittest.main()
