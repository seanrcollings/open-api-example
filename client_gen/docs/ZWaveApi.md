# swagger_client.ZWaveApi

All URIs are relative to *https://virtserver.swaggerhub.com/sean.collings/DemoAPI/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lighting_summary**](ZWaveApi.md#get_lighting_summary) | **GET** /lightingSummary | 
[**get_switch_state**](ZWaveApi.md#get_switch_state) | **GET** /lighting/switches/{deviceId} | 
[**set_dimmer**](ZWaveApi.md#set_dimmer) | **POST** /lighting/dimmers/{deviceId}/{value} | 
[**set_dimmer_timer**](ZWaveApi.md#set_dimmer_timer) | **POST** /lighting/dimmers/{deviceId}/{value}/timer/{timeunit} | 
[**set_switch**](ZWaveApi.md#set_switch) | **POST** /lighting/switches/{deviceId}/{value} | 
[**set_switch_timer**](ZWaveApi.md#set_switch_timer) | **POST** /lighting/switches/{deviceId}/{value}/timer/{minutes} | 

# **get_lighting_summary**
> LightingSummary get_lighting_summary()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ZWaveApi()

try:
    api_response = api_instance.get_lighting_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZWaveApi->get_lighting_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LightingSummary**](LightingSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_switch_state**
> DeviceState get_switch_state(device_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ZWaveApi()
device_id = 'device_id_example' # str | 

try:
    api_response = api_instance.get_switch_state(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZWaveApi->get_switch_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

[**DeviceState**](DeviceState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_dimmer**
> ApiResponse set_dimmer(device_id, value)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ZWaveApi()
device_id = 'device_id_example' # str | 
value = 56 # int | 

try:
    api_response = api_instance.set_dimmer(device_id, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZWaveApi->set_dimmer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **value** | **int**|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_dimmer_timer**
> ApiResponse set_dimmer_timer(device_id, value, timeunit, units=units)



sets a dimmer to a specific value on a timer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ZWaveApi()
device_id = 'device_id_example' # str | 
value = 56 # int | 
timeunit = 56 # int | 
units = 'milliseconds' # str |  (optional) (default to milliseconds)

try:
    api_response = api_instance.set_dimmer_timer(device_id, value, timeunit, units=units)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZWaveApi->set_dimmer_timer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **value** | **int**|  | 
 **timeunit** | **int**|  | 
 **units** | **str**|  | [optional] [default to milliseconds]

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_switch**
> ApiResponse set_switch(device_id, value)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ZWaveApi()
device_id = 'device_id_example' # str | 
value = 'value_example' # str | 

try:
    api_response = api_instance.set_switch(device_id, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZWaveApi->set_switch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **value** | **str**|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_switch_timer**
> ApiResponse set_switch_timer(device_id, value, minutes)



sets a switch to a specific value on a timer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ZWaveApi()
device_id = 'device_id_example' # str | 
value = 'value_example' # str | 
minutes = 56 # int | 

try:
    api_response = api_instance.set_switch_timer(device_id, value, minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZWaveApi->set_switch_timer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **value** | **str**|  | 
 **minutes** | **int**|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

