# openapi_client.AstuApi

All URIs are relative to *http://https:/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**process_objects**](AstuApi.md#process_objects) | **POST** /astu/import | Отправка объектов на обработку
[**search_objects**](AstuApi.md#search_objects) | **POST** /astu/export | Запрос поиска объектов


# **process_objects**
> List[ConsumersInner] process_objects(service_location)

Отправка объектов на обработку

Отправка объектов на обработку

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.consumers_inner import ConsumersInner
from openapi_client.models.service_location import ServiceLocation
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https:/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://https:/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AstuApi(api_client)
    service_location = openapi_client.ServiceLocation() # ServiceLocation | Параметры обращения к сервису - определяются проектным решением для каждого сервиса индивидуально

    try:
        # Отправка объектов на обработку
        api_response = api_instance.process_objects(service_location)
        print("The response of AstuApi->process_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AstuApi->process_objects: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_location** | [**ServiceLocation**](ServiceLocation.md)| Параметры обращения к сервису - определяются проектным решением для каждого сервиса индивидуально | 

### Return type

[**List[ConsumersInner]**](ConsumersInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | результаты поиска по запросу - определяются проектным решением для каждого сервиса индивидуально |  -  |
**400** | не верные параметры сервиса или объекта запроса |  -  |
**429** | АСТУ сформировало запросов больше чем описано в требованиях |  -  |
**204** | витрину с данными не заполена или изменений нет |  -  |
**408** | JSON формируется больше 1  мин |  -  |
**500** | Server Error |  -  |
**409** | Conflict |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_objects**
> List[ConsumersInner] search_objects(end_device_request_body, limit=limit, offset=offset)

Запрос поиска объектов

Запрос поиска объектов по заданному сервису

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.consumers_inner import ConsumersInner
from openapi_client.models.end_device_request_body import EndDeviceRequestBody
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https:/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://https:/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AstuApi(api_client)
    end_device_request_body = openapi_client.EndDeviceRequestBody() # EndDeviceRequestBody | Параметры обращения к сервису - определяются проектным решением для каждого сервиса индивидуально
    limit = 0 # int | кол-во элементов от начала отсчета (optional)
    offset = 0 # int | индекс начала отчета (optional)

    try:
        # Запрос поиска объектов
        api_response = api_instance.search_objects(end_device_request_body, limit=limit, offset=offset)
        print("The response of AstuApi->search_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AstuApi->search_objects: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_device_request_body** | [**EndDeviceRequestBody**](EndDeviceRequestBody.md)| Параметры обращения к сервису - определяются проектным решением для каждого сервиса индивидуально | 
 **limit** | **int**| кол-во элементов от начала отсчета | [optional] 
 **offset** | **int**| индекс начала отчета | [optional] 

### Return type

[**List[ConsumersInner]**](ConsumersInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | результаты поиска по запросу - определяются проектным решением для каждого сервиса индивидуально |  -  |
**400** | не верные параметры сервиса или объекта запроса |  -  |
**429** | АСТУ сформировало запросов больше чем описано в требованиях |  -  |
**204** | витрину с данными не заполена или изменений нет |  -  |
**408** | JSON формируется больше 1  мин |  -  |
**500** | Server Error |  -  |
**409** | Conflict |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

