# ConsumersRequestBody

2.1 Параметры тела запроса для сервиса Consumers

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | [**Service**](Service.md) |  | 
**params** | [**ConsumersRequestBodyParams**](ConsumersRequestBodyParams.md) |  | 

## Example

```python
from openapi_client.models.consumers_request_body import ConsumersRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumersRequestBody from a JSON string
consumers_request_body_instance = ConsumersRequestBody.from_json(json)
# print the JSON string representation of the object
print ConsumersRequestBody.to_json()

# convert the object into a dict
consumers_request_body_dict = consumers_request_body_instance.to_dict()
# create an instance of ConsumersRequestBody from a dict
consumers_request_body_form_dict = consumers_request_body.from_dict(consumers_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


