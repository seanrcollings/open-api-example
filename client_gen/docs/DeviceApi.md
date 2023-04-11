# swagger_client.DeviceApi

All URIs are relative to *https://virtserver.swaggerhub.com/sean.collings/DemoAPI/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_devices**](DeviceApi.md#get_devices) | **GET** /devices | 
[**register**](DeviceApi.md#register) | **POST** /devices | 

# **get_devices**
> list[str] get_devices(skip=skip, limit=limit)



returns all registered devices

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceApi()
skip = 56 # int | number of records to skip (optional)
limit = 56 # int | max number of records to return (optional)

try:
    api_response = api_instance.get_devices(skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->get_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| number of records to skip | [optional] 
 **limit** | **int**| max number of records to return | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register**
> register(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceApi()
body = swagger_client.DeviceRegistrationInfo() # DeviceRegistrationInfo |  (optional)

try:
    api_instance.register(body=body)
except ApiException as e:
    print("Exception when calling DeviceApi->register: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceRegistrationInfo**](DeviceRegistrationInfo.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

