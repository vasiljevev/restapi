# DisconnectionReconnectionRequestBody

4.1 Параметры тела запроса для сервиса Disconnection/Reconnection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | [**Service**](Service.md) |  | 
**params** | [**DisconnectionReconnectionRequestBodyParams**](DisconnectionReconnectionRequestBodyParams.md) |  | 

## Example

```python
from openapi_client.models.disconnection_reconnection_request_body import DisconnectionReconnectionRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of DisconnectionReconnectionRequestBody from a JSON string
disconnection_reconnection_request_body_instance = DisconnectionReconnectionRequestBody.from_json(json)
# print the JSON string representation of the object
print DisconnectionReconnectionRequestBody.to_json()

# convert the object into a dict
disconnection_reconnection_request_body_dict = disconnection_reconnection_request_body_instance.to_dict()
# create an instance of DisconnectionReconnectionRequestBody from a dict
disconnection_reconnection_request_body_form_dict = disconnection_reconnection_request_body.from_dict(disconnection_reconnection_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


