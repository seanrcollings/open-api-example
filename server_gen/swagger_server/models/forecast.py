# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.forecast_temperature import ForecastTemperature  # noqa: F401,E501
from swagger_server.models.weather_forecast import WeatherForecast  # noqa: F401,E501
from swagger_server import util


class Forecast(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, _date: datetime=None, pressure: float=None, humidity: int=None, wind_speed: float=None, clouds: int=None, temperature: ForecastTemperature=None, weather: WeatherForecast=None):  # noqa: E501
        """Forecast - a model defined in Swagger

        :param _date: The _date of this Forecast.  # noqa: E501
        :type _date: datetime
        :param pressure: The pressure of this Forecast.  # noqa: E501
        :type pressure: float
        :param humidity: The humidity of this Forecast.  # noqa: E501
        :type humidity: int
        :param wind_speed: The wind_speed of this Forecast.  # noqa: E501
        :type wind_speed: float
        :param clouds: The clouds of this Forecast.  # noqa: E501
        :type clouds: int
        :param temperature: The temperature of this Forecast.  # noqa: E501
        :type temperature: ForecastTemperature
        :param weather: The weather of this Forecast.  # noqa: E501
        :type weather: WeatherForecast
        """
        self.swagger_types = {
            '_date': datetime,
            'pressure': float,
            'humidity': int,
            'wind_speed': float,
            'clouds': int,
            'temperature': ForecastTemperature,
            'weather': WeatherForecast
        }

        self.attribute_map = {
            '_date': 'date',
            'pressure': 'pressure',
            'humidity': 'humidity',
            'wind_speed': 'windSpeed',
            'clouds': 'clouds',
            'temperature': 'temperature',
            'weather': 'weather'
        }
        self.__date = _date
        self._pressure = pressure
        self._humidity = humidity
        self._wind_speed = wind_speed
        self._clouds = clouds
        self._temperature = temperature
        self._weather = weather

    @classmethod
    def from_dict(cls, dikt) -> 'Forecast':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Forecast of this Forecast.  # noqa: E501
        :rtype: Forecast
        """
        return util.deserialize_model(dikt, cls)

    @property
    def _date(self) -> datetime:
        """Gets the _date of this Forecast.


        :return: The _date of this Forecast.
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date: datetime):
        """Sets the _date of this Forecast.


        :param _date: The _date of this Forecast.
        :type _date: datetime
        """

        self.__date = _date

    @property
    def pressure(self) -> float:
        """Gets the pressure of this Forecast.


        :return: The pressure of this Forecast.
        :rtype: float
        """
        return self._pressure

    @pressure.setter
    def pressure(self, pressure: float):
        """Sets the pressure of this Forecast.


        :param pressure: The pressure of this Forecast.
        :type pressure: float
        """

        self._pressure = pressure

    @property
    def humidity(self) -> int:
        """Gets the humidity of this Forecast.


        :return: The humidity of this Forecast.
        :rtype: int
        """
        return self._humidity

    @humidity.setter
    def humidity(self, humidity: int):
        """Sets the humidity of this Forecast.


        :param humidity: The humidity of this Forecast.
        :type humidity: int
        """

        self._humidity = humidity

    @property
    def wind_speed(self) -> float:
        """Gets the wind_speed of this Forecast.


        :return: The wind_speed of this Forecast.
        :rtype: float
        """
        return self._wind_speed

    @wind_speed.setter
    def wind_speed(self, wind_speed: float):
        """Sets the wind_speed of this Forecast.


        :param wind_speed: The wind_speed of this Forecast.
        :type wind_speed: float
        """

        self._wind_speed = wind_speed

    @property
    def clouds(self) -> int:
        """Gets the clouds of this Forecast.


        :return: The clouds of this Forecast.
        :rtype: int
        """
        return self._clouds

    @clouds.setter
    def clouds(self, clouds: int):
        """Sets the clouds of this Forecast.


        :param clouds: The clouds of this Forecast.
        :type clouds: int
        """

        self._clouds = clouds

    @property
    def temperature(self) -> ForecastTemperature:
        """Gets the temperature of this Forecast.


        :return: The temperature of this Forecast.
        :rtype: ForecastTemperature
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature: ForecastTemperature):
        """Sets the temperature of this Forecast.


        :param temperature: The temperature of this Forecast.
        :type temperature: ForecastTemperature
        """

        self._temperature = temperature

    @property
    def weather(self) -> WeatherForecast:
        """Gets the weather of this Forecast.


        :return: The weather of this Forecast.
        :rtype: WeatherForecast
        """
        return self._weather

    @weather.setter
    def weather(self, weather: WeatherForecast):
        """Sets the weather of this Forecast.


        :param weather: The weather of this Forecast.
        :type weather: WeatherForecast
        """

        self._weather = weather