# DisconnectionReconnectionRequestBodyParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_begin** | **date** | Начальная дата анализа данных по потребителям | 
**date_end** | **date** | Начальная дата анализа данных по потребителям | 

## Example

```python
from openapi_client.models.disconnection_reconnection_request_body_params import DisconnectionReconnectionRequestBodyParams

# TODO update the JSON string below
json = "{}"
# create an instance of DisconnectionReconnectionRequestBodyParams from a JSON string
disconnection_reconnection_request_body_params_instance = DisconnectionReconnectionRequestBodyParams.from_json(json)
# print the JSON string representation of the object
print DisconnectionReconnectionRequestBodyParams.to_json()

# convert the object into a dict
disconnection_reconnection_request_body_params_dict = disconnection_reconnection_request_body_params_instance.to_dict()
# create an instance of DisconnectionReconnectionRequestBodyParams from a dict
disconnection_reconnection_request_body_params_form_dict = disconnection_reconnection_request_body_params.from_dict(disconnection_reconnection_request_body_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


