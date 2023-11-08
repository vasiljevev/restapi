# ConsumersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | **str** |  | [optional] 
**consumer_id** | **str** |  | [optional] 
**consumer_name** | **str** |  | [optional] 
**consumer_type** | **str** |  | [optional] 
**contract** | **str** |  | [optional] 
**requets_number** | **str** |  | [optional] 
**service_location_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**object_status** | **str** |  | [optional] 
**fias_id** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**district** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**street** | **str** |  | [optional] 
**house** | **str** |  | [optional] 
**room** | **str** |  | [optional] 
**remark** | **str** |  | [optional] 
**cadaster** | **str** |  | [optional] 
**max_power** | **str** |  | [optional] 
**reliability_category** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**residents_count** | **str** |  | [optional] 
**service_disp_category** | **str** |  | [optional] 
**num_of_storeys** | **str** |  | [optional] 
**stand_by_capacity** | **str** |  | [optional] 
**significance** | **str** |  | [optional] 
**service_contingency_catagory** | **str** |  | [optional] 
**in_charge_full_name** | **str** |  | [optional] 
**emergency_power_reserve** | **str** |  | [optional] 
**techno_power_reserve** | **str** |  | [optional] 
**techno_power_reserve_duration** | **str** |  | [optional] 
**geometry** | [**Geometry**](Geometry.md) |  | [optional] 
**usage_points** | [**List[ConsumersInnerUsagePointsInner]**](ConsumersInnerUsagePointsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.consumers_inner import ConsumersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumersInner from a JSON string
consumers_inner_instance = ConsumersInner.from_json(json)
# print the JSON string representation of the object
print ConsumersInner.to_json()

# convert the object into a dict
consumers_inner_dict = consumers_inner_instance.to_dict()
# create an instance of ConsumersInner from a dict
consumers_inner_form_dict = consumers_inner.from_dict(consumers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


