# ServiceLocationAddress

Адресная информация

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Полный адрес (до дома) | [optional] 
**region** | **str** | Регион | [optional] 
**district** | **str** | Район | [optional] 
**city** | **str** | Город | [optional] 
**street** | **str** | Улица | [optional] 
**house** | **str** | Дом | [optional] 

## Example

```python
from openapi_client.models.service_location_address import ServiceLocationAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLocationAddress from a JSON string
service_location_address_instance = ServiceLocationAddress.from_json(json)
# print the JSON string representation of the object
print ServiceLocationAddress.to_json()

# convert the object into a dict
service_location_address_dict = service_location_address_instance.to_dict()
# create an instance of ServiceLocationAddress from a dict
service_location_address_form_dict = service_location_address.from_dict(service_location_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


