# openapi-client
Интеграционный сервис АИС КИС Баланс

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.example.com/support](https://www.example.com/support)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
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
    except ApiException as e:
        print("Exception when calling AstuApi->process_objects: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://https:/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AstuApi* | [**process_objects**](docs/AstuApi.md#process_objects) | **POST** /astu/import | Отправка объектов на обработку
*AstuApi* | [**search_objects**](docs/AstuApi.md#search_objects) | **POST** /astu/export | Запрос поиска объектов


## Documentation For Models

 - [ConsumersInner](docs/ConsumersInner.md)
 - [ConsumersInnerUsagePointsInner](docs/ConsumersInnerUsagePointsInner.md)
 - [ConsumersRequestBody](docs/ConsumersRequestBody.md)
 - [ConsumersRequestBodyParams](docs/ConsumersRequestBodyParams.md)
 - [DisconnectionReconnection](docs/DisconnectionReconnection.md)
 - [DisconnectionReconnectionDisconnectionListInner](docs/DisconnectionReconnectionDisconnectionListInner.md)
 - [DisconnectionReconnectionDisconnectionListInnerUsagePointsInner](docs/DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.md)
 - [DisconnectionReconnectionReconnectionListInner](docs/DisconnectionReconnectionReconnectionListInner.md)
 - [DisconnectionReconnectionRequestBody](docs/DisconnectionReconnectionRequestBody.md)
 - [DisconnectionReconnectionRequestBodyParams](docs/DisconnectionReconnectionRequestBodyParams.md)
 - [EndDeviceRequestBody](docs/EndDeviceRequestBody.md)
 - [EndDeviceRequestBodyParams](docs/EndDeviceRequestBodyParams.md)
 - [EndDevicesInner](docs/EndDevicesInner.md)
 - [EndDevicesInnerMeasurePointsInner](docs/EndDevicesInnerMeasurePointsInner.md)
 - [Geometry](docs/Geometry.md)
 - [GeometryCoordinatesInner](docs/GeometryCoordinatesInner.md)
 - [Service](docs/Service.md)
 - [ServiceLocation](docs/ServiceLocation.md)
 - [ServiceLocationAddress](docs/ServiceLocationAddress.md)
 - [ServiceLocationCadatster](docs/ServiceLocationCadatster.md)
 - [UsagePoint](docs/UsagePoint.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author

e-vasilyev@it-serv.ru

