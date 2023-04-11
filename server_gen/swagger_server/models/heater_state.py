# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class HeaterState(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, state: str=None):  # noqa: E501
        """HeaterState - a model defined in Swagger

        :param id: The id of this HeaterState.  # noqa: E501
        :type id: str
        :param state: The state of this HeaterState.  # noqa: E501
        :type state: str
        """
        self.swagger_types = {
            'id': str,
            'state': str
        }

        self.attribute_map = {
            'id': 'id',
            'state': 'state'
        }
        self._id = id
        self._state = state

    @classmethod
    def from_dict(cls, dikt) -> 'HeaterState':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HeaterState of this HeaterState.  # noqa: E501
        :rtype: HeaterState
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this HeaterState.


        :return: The id of this HeaterState.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this HeaterState.


        :param id: The id of this HeaterState.
        :type id: str
        """

        self._id = id

    @property
    def state(self) -> str:
        """Gets the state of this HeaterState.


        :return: The state of this HeaterState.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """Sets the state of this HeaterState.


        :param state: The state of this HeaterState.
        :type state: str
        """

        self._state = state