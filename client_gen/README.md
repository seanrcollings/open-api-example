# swagger-client
The API for the EatBacon IOT project

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceApi(swagger_client.ApiClient(configuration))
skip = 56 # int | number of records to skip (optional)
limit = 56 # int | max number of records to return (optional)

try:
    api_response = api_instance.get_devices(skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->get_devices: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DeviceApi(swagger_client.ApiClient(configuration))
body = swagger_client.DeviceRegistrationInfo() # DeviceRegistrationInfo |  (optional)

try:
    api_instance.register(body=body)
except ApiException as e:
    print("Exception when calling DeviceApi->register: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://virtserver.swaggerhub.com/sean.collings/DemoAPI/1.0.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DeviceApi* | [**get_devices**](docs/DeviceApi.md#get_devices) | **GET** /devices | 
*DeviceApi* | [**register**](docs/DeviceApi.md#register) | **POST** /devices | 
*EnvironmentApi* | [**get_forecast**](docs/EnvironmentApi.md#get_forecast) | **GET** /temperature/forecast/{days} | 
*EnvironmentApi* | [**get_heater_state**](docs/EnvironmentApi.md#get_heater_state) | **GET** /temperature/{zoneId}/heater | 
*EnvironmentApi* | [**get_zone_temperature**](docs/EnvironmentApi.md#get_zone_temperature) | **GET** /temperature/{zoneId} | 
*EnvironmentApi* | [**set_heater_state**](docs/EnvironmentApi.md#set_heater_state) | **POST** /temperature/{zoneId}/heater/{state} | 
*EnvironmentApi* | [**temperature_summary**](docs/EnvironmentApi.md#temperature_summary) | **GET** /temperature | 
*ZWaveApi* | [**get_lighting_summary**](docs/ZWaveApi.md#get_lighting_summary) | **GET** /lightingSummary | 
*ZWaveApi* | [**get_switch_state**](docs/ZWaveApi.md#get_switch_state) | **GET** /lighting/switches/{deviceId} | 
*ZWaveApi* | [**set_dimmer**](docs/ZWaveApi.md#set_dimmer) | **POST** /lighting/dimmers/{deviceId}/{value} | 
*ZWaveApi* | [**set_dimmer_timer**](docs/ZWaveApi.md#set_dimmer_timer) | **POST** /lighting/dimmers/{deviceId}/{value}/timer/{timeunit} | 
*ZWaveApi* | [**set_switch**](docs/ZWaveApi.md#set_switch) | **POST** /lighting/switches/{deviceId}/{value} | 
*ZWaveApi* | [**set_switch_timer**](docs/ZWaveApi.md#set_switch_timer) | **POST** /lighting/switches/{deviceId}/{value}/timer/{minutes} | 
*ZonesApi* | [**get_zones**](docs/ZonesApi.md#get_zones) | **GET** /zones | 
*ZonesApi* | [**quiet_zone**](docs/ZonesApi.md#quiet_zone) | **GET** /zones/{zoneId}/quiet | 

## Documentation For Models

 - [ApiResponse](docs/ApiResponse.md)
 - [City](docs/City.md)
 - [DeviceRegistrationInfo](docs/DeviceRegistrationInfo.md)
 - [DeviceState](docs/DeviceState.md)
 - [Forecast](docs/Forecast.md)
 - [ForecastResponse](docs/ForecastResponse.md)
 - [ForecastTemperature](docs/ForecastTemperature.md)
 - [HeaterState](docs/HeaterState.md)
 - [LightingSummary](docs/LightingSummary.md)
 - [LightingZone](docs/LightingZone.md)
 - [LightingZoneStatus](docs/LightingZoneStatus.md)
 - [TemperatueZoneStatus](docs/TemperatueZoneStatus.md)
 - [TemperatureSummary](docs/TemperatureSummary.md)
 - [TemperatureZone](docs/TemperatureZone.md)
 - [WeatherForecast](docs/WeatherForecast.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author


