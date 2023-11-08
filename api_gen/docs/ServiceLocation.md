# ServiceLocation

3.1 используется для передачи в КИС Баланс из ПТК АСТУ данных по скорректированному местоположению ЭПУ потребителя

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | [**Service**](Service.md) |  | 
**consumer_id** | **str** | Идентификатор Потребителя КИС Баланс | 
**service_location_id** | **str** | Идентификатор ЭПУ КИС Баланс | 
**address** | [**ServiceLocationAddress**](ServiceLocationAddress.md) |  | [optional] 
**cadatster** | [**ServiceLocationCadatster**](ServiceLocationCadatster.md) |  | [optional] 
**geometry** | [**Geometry**](Geometry.md) |  | 

## Example

```python
from openapi_client.models.service_location import ServiceLocation

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLocation from a JSON string
service_location_instance = ServiceLocation.from_json(json)
# print the JSON string representation of the object
print ServiceLocation.to_json()

# convert the object into a dict
service_location_dict = service_location_instance.to_dict()
# create an instance of ServiceLocation from a dict
service_location_form_dict = service_location.from_dict(service_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


