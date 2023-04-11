# swagger_client.EnvironmentApi

All URIs are relative to *https://virtserver.swaggerhub.com/sean.collings/DemoAPI/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_forecast**](EnvironmentApi.md#get_forecast) | **GET** /temperature/forecast/{days} | 
[**get_heater_state**](EnvironmentApi.md#get_heater_state) | **GET** /temperature/{zoneId}/heater | 
[**get_zone_temperature**](EnvironmentApi.md#get_zone_temperature) | **GET** /temperature/{zoneId} | 
[**set_heater_state**](EnvironmentApi.md#set_heater_state) | **POST** /temperature/{zoneId}/heater/{state} | 
[**temperature_summary**](EnvironmentApi.md#temperature_summary) | **GET** /temperature | 

# **get_forecast**
> ForecastResponse get_forecast(days)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnvironmentApi()
days = 56 # int | 

try:
    api_response = api_instance.get_forecast(days)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->get_forecast: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**|  | 

### Return type

[**ForecastResponse**](ForecastResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heater_state**
> HeaterState get_heater_state(zone_id)



gets the state of the heater

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnvironmentApi()
zone_id = 'zone_id_example' # str | 

try:
    api_response = api_instance.get_heater_state(zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->get_heater_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**|  | 

### Return type

[**HeaterState**](HeaterState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_temperature**
> TemperatueZoneStatus get_zone_temperature(zone_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnvironmentApi()
zone_id = 'zone_id_example' # str | 

try:
    api_response = api_instance.get_zone_temperature(zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->get_zone_temperature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**|  | 

### Return type

[**TemperatueZoneStatus**](TemperatueZoneStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_heater_state**
> ApiResponse set_heater_state(zone_id, state)



turns the heater on or off

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnvironmentApi()
zone_id = 'zone_id_example' # str | 
state = 'state_example' # str | 

try:
    api_response = api_instance.set_heater_state(zone_id, state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->set_heater_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**|  | 
 **state** | **str**|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **temperature_summary**
> TemperatureSummary temperature_summary()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EnvironmentApi()

try:
    api_response = api_instance.temperature_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->temperature_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TemperatureSummary**](TemperatureSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

