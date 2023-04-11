# swagger_client.ZonesApi

All URIs are relative to *https://virtserver.swaggerhub.com/sean.collings/DemoAPI/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_zones**](ZonesApi.md#get_zones) | **GET** /zones | 
[**quiet_zone**](ZonesApi.md#quiet_zone) | **GET** /zones/{zoneId}/quiet | 

# **get_zones**
> list[str] get_zones()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ZonesApi()

try:
    api_response = api_instance.get_zones()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonesApi->get_zones: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quiet_zone**
> quiet_zone(zone_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ZonesApi()
zone_id = 'zone_id_example' # str | 

try:
    api_instance.quiet_zone(zone_id)
except ApiException as e:
    print("Exception when calling ZonesApi->quiet_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

