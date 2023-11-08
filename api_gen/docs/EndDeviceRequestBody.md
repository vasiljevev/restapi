# EndDeviceRequestBody

5.1 Параметры тела запроса для сервиса EndDevice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | [**Service**](Service.md) |  | 
**params** | [**EndDeviceRequestBodyParams**](EndDeviceRequestBodyParams.md) |  | 

## Example

```python
from openapi_client.models.end_device_request_body import EndDeviceRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of EndDeviceRequestBody from a JSON string
end_device_request_body_instance = EndDeviceRequestBody.from_json(json)
# print the JSON string representation of the object
print EndDeviceRequestBody.to_json()

# convert the object into a dict
end_device_request_body_dict = end_device_request_body_instance.to_dict()
# create an instance of EndDeviceRequestBody from a dict
end_device_request_body_form_dict = end_device_request_body.from_dict(end_device_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


