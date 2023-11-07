# ConsumersInnerUsagePointsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | **str** |  | [optional] 
**usage_point_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**is_sdp** | **bool** |  | [optional] 
**voltage_level** | **str** |  | [optional] 
**voltage_class** | **str** |  | [optional] 
**service_location_id** | **str** |  | [optional] 
**substation_code_tm** | **str** |  | [optional] 
**substation_name** | **str** |  | [optional] 
**transformer_name** | **str** |  | [optional] 
**bay_code_tm** | **str** |  | [optional] 
**bay_name** | **str** |  | [optional] 
**line_code_tm** | **str** |  | [optional] 
**line_name** | **str** |  | [optional] 
**tower_code_tm** | **str** |  | [optional] 
**tower_name** | **str** |  | [optional] 
**remark** | **str** |  | [optional] 
**geometry** | [**Geometry**](Geometry.md) |  | [optional] 

## Example

```python
from openapi_client.models.consumers_inner_usage_points_inner import ConsumersInnerUsagePointsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumersInnerUsagePointsInner from a JSON string
consumers_inner_usage_points_inner_instance = ConsumersInnerUsagePointsInner.from_json(json)
# print the JSON string representation of the object
print ConsumersInnerUsagePointsInner.to_json()

# convert the object into a dict
consumers_inner_usage_points_inner_dict = consumers_inner_usage_points_inner_instance.to_dict()
# create an instance of ConsumersInnerUsagePointsInner from a dict
consumers_inner_usage_points_inner_form_dict = consumers_inner_usage_points_inner.from_dict(consumers_inner_usage_points_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


