# UsagePoint

3.2 Сервис используется для передачи в КИС Баланс из ПТК АСТУ данных по скорректированной привязке потребителя к объекту электросети

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | [**Service**](Service.md) |  | 
**usage_point_id** | **str** | Идентификатор Точки поставки в КИС Баланс | 
**service_location_id** | **str** | Идентификатор ЭПУ КИС Баланс | [optional] 
**substation_code_tm** | **str** | Код ТМ СУПА питающей подстанции (ТП/РП) | 
**transformer_name** | **str** | Наименование питающего трансформатора | [optional] 
**bay_code_tm** | **str** | Код КМ СУПА ячейки присоединения питающего фидера | [optional] 
**bay_name** | **str** |  | [optional] 
**line_code_tm** | **str** |  | [optional] 
**line_name** | **str** |  | [optional] 
**tower_code_tm** | **str** |  | [optional] 
**tower_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.usage_point import UsagePoint

# TODO update the JSON string below
json = "{}"
# create an instance of UsagePoint from a JSON string
usage_point_instance = UsagePoint.from_json(json)
# print the JSON string representation of the object
print UsagePoint.to_json()

# convert the object into a dict
usage_point_dict = usage_point_instance.to_dict()
# create an instance of UsagePoint from a dict
usage_point_form_dict = usage_point.from_dict(usage_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


