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

class TemperatureZone(object):
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
        'id': 'int',
        'name': 'str',
        'input_position': 'int',
        'output_position': 'int',
        'zone': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'input_position': 'inputPosition',
        'output_position': 'outputPosition',
        'zone': 'zone'
    }

    def __init__(self, id=None, name=None, input_position=None, output_position=None, zone=None):  # noqa: E501
        """TemperatureZone - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._input_position = None
        self._output_position = None
        self._zone = None
        self.discriminator = None
        self.id = id
        self.name = name
        if input_position is not None:
            self.input_position = input_position
        if output_position is not None:
            self.output_position = output_position
        if zone is not None:
            self.zone = zone

    @property
    def id(self):
        """Gets the id of this TemperatureZone.  # noqa: E501

        the unique identifier for the zone  # noqa: E501

        :return: The id of this TemperatureZone.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TemperatureZone.

        the unique identifier for the zone  # noqa: E501

        :param id: The id of this TemperatureZone.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this TemperatureZone.  # noqa: E501


        :return: The name of this TemperatureZone.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TemperatureZone.


        :param name: The name of this TemperatureZone.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def input_position(self):
        """Gets the input_position of this TemperatureZone.  # noqa: E501


        :return: The input_position of this TemperatureZone.  # noqa: E501
        :rtype: int
        """
        return self._input_position

    @input_position.setter
    def input_position(self, input_position):
        """Sets the input_position of this TemperatureZone.


        :param input_position: The input_position of this TemperatureZone.  # noqa: E501
        :type: int
        """

        self._input_position = input_position

    @property
    def output_position(self):
        """Gets the output_position of this TemperatureZone.  # noqa: E501


        :return: The output_position of this TemperatureZone.  # noqa: E501
        :rtype: int
        """
        return self._output_position

    @output_position.setter
    def output_position(self, output_position):
        """Sets the output_position of this TemperatureZone.


        :param output_position: The output_position of this TemperatureZone.  # noqa: E501
        :type: int
        """

        self._output_position = output_position

    @property
    def zone(self):
        """Gets the zone of this TemperatureZone.  # noqa: E501


        :return: The zone of this TemperatureZone.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this TemperatureZone.


        :param zone: The zone of this TemperatureZone.  # noqa: E501
        :type: str
        """

        self._zone = zone

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
        if issubclass(TemperatureZone, dict):
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
        if not isinstance(other, TemperatureZone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
