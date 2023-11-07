# EndDeviceRequestBodyParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumption_type** | **str** | Вид учета (flow - технический, estim - коммерческий) | [optional] 
**device_type** | **List[str]** |  | [optional] 
**date_begin** | **date** | Начальная дата анализа данных по потребителям | [optional] 
**date_end** | **date** | Начальная дата анализа данных по потребителям | [optional] 
**usage_point_id** | **List[str]** | Массив идентификаторов точек поставки | [optional] 
**device_id_id** | **List[str]** | Массив идентификаторов приборов учета | [optional] 
**system_state** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.end_device_request_body_params import EndDeviceRequestBodyParams

# TODO update the JSON string below
json = "{}"
# create an instance of EndDeviceRequestBodyParams from a JSON string
end_device_request_body_params_instance = EndDeviceRequestBodyParams.from_json(json)
# print the JSON string representation of the object
print EndDeviceRequestBodyParams.to_json()

# convert the object into a dict
end_device_request_body_params_dict = end_device_request_body_params_instance.to_dict()
# create an instance of EndDeviceRequestBodyParams from a dict
end_device_request_body_params_form_dict = end_device_request_body_params.from_dict(end_device_request_body_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


