# ConsumersRequestBodyParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Тип потребителя (ФЛ, ЮЛ) из справочника КИС Баланс | [optional] 
**date_begin** | **date** | Начальная дата анализа данных по потребителям | [optional] 
**date_end** | **date** | Конечная дата анализа данных по потребителям | [optional] 
**consumer_id** | **List[str]** |  | [optional] 
**service_location_id** | **List[str]** |  | [optional] 
**system_state** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.consumers_request_body_params import ConsumersRequestBodyParams

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumersRequestBodyParams from a JSON string
consumers_request_body_params_instance = ConsumersRequestBodyParams.from_json(json)
# print the JSON string representation of the object
print ConsumersRequestBodyParams.to_json()

# convert the object into a dict
consumers_request_body_params_dict = consumers_request_body_params_instance.to_dict()
# create an instance of ConsumersRequestBodyParams from a dict
consumers_request_body_params_form_dict = consumers_request_body_params.from_dict(consumers_request_body_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


