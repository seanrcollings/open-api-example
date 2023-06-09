# coding: utf-8

"""
    home-iot-api

    The API for the EatBacon IOT project  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ForecastTemperature(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'low': 'float',
        'high': 'float',
        'morning': 'float',
        'day': 'float',
        'evening': 'float',
        'night': 'float'
    }

    attribute_map = {
        'low': 'low',
        'high': 'high',
        'morning': 'morning',
        'day': 'day',
        'evening': 'evening',
        'night': 'night'
    }

    def __init__(self, low=None, high=None, morning=None, day=None, evening=None, night=None):  # noqa: E501
        """ForecastTemperature - a model defined in Swagger"""  # noqa: E501
        self._low = None
        self._high = None
        self._morning = None
        self._day = None
        self._evening = None
        self._night = None
        self.discriminator = None
        if low is not None:
            self.low = low
        if high is not None:
            self.high = high
        if morning is not None:
            self.morning = morning
        if day is not None:
            self.day = day
        if evening is not None:
            self.evening = evening
        if night is not None:
            self.night = night

    @property
    def low(self):
        """Gets the low of this ForecastTemperature.  # noqa: E501


        :return: The low of this ForecastTemperature.  # noqa: E501
        :rtype: float
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this ForecastTemperature.


        :param low: The low of this ForecastTemperature.  # noqa: E501
        :type: float
        """

        self._low = low

    @property
    def high(self):
        """Gets the high of this ForecastTemperature.  # noqa: E501


        :return: The high of this ForecastTemperature.  # noqa: E501
        :rtype: float
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this ForecastTemperature.


        :param high: The high of this ForecastTemperature.  # noqa: E501
        :type: float
        """

        self._high = high

    @property
    def morning(self):
        """Gets the morning of this ForecastTemperature.  # noqa: E501


        :return: The morning of this ForecastTemperature.  # noqa: E501
        :rtype: float
        """
        return self._morning

    @morning.setter
    def morning(self, morning):
        """Sets the morning of this ForecastTemperature.


        :param morning: The morning of this ForecastTemperature.  # noqa: E501
        :type: float
        """

        self._morning = morning

    @property
    def day(self):
        """Gets the day of this ForecastTemperature.  # noqa: E501


        :return: The day of this ForecastTemperature.  # noqa: E501
        :rtype: float
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this ForecastTemperature.


        :param day: The day of this ForecastTemperature.  # noqa: E501
        :type: float
        """

        self._day = day

    @property
    def evening(self):
        """Gets the evening of this ForecastTemperature.  # noqa: E501


        :return: The evening of this ForecastTemperature.  # noqa: E501
        :rtype: float
        """
        return self._evening

    @evening.setter
    def evening(self, evening):
        """Sets the evening of this ForecastTemperature.


        :param evening: The evening of this ForecastTemperature.  # noqa: E501
        :type: float
        """

        self._evening = evening

    @property
    def night(self):
        """Gets the night of this ForecastTemperature.  # noqa: E501


        :return: The night of this ForecastTemperature.  # noqa: E501
        :rtype: float
        """
        return self._night

    @night.setter
    def night(self, night):
        """Sets the night of this ForecastTemperature.


        :param night: The night of this ForecastTemperature.  # noqa: E501
        :type: float
        """

        self._night = night

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ForecastTemperature, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ForecastTemperature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
