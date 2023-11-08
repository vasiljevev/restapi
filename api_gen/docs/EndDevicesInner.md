# EndDevicesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | **str** |  | [optional] 
**end_device_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**device_type** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**is_amr** | **str** |  | [optional] 
**is_commercial** | **str** |  | [optional] 
**device_status** | **str** |  | [optional] 
**belonging_type** | **str** |  | [optional] 
**usage_point_id** | **str** |  | [optional] 
**substation_code_tm** | **str** |  | [optional] 
**bay_code_tm** | **str** |  | [optional] 
**line_code_tm** | **str** |  | [optional] 
**tower_code_tm** | **str** |  | [optional] 
**device_location** | **str** |  | [optional] 
**geometry** | [**Geometry**](Geometry.md) |  | [optional] 
**measure_points** | [**List[EndDevicesInnerMeasurePointsInner]**](EndDevicesInnerMeasurePointsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.end_devices_inner import EndDevicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of EndDevicesInner from a JSON string
end_devices_inner_instance = EndDevicesInner.from_json(json)
# print the JSON string representation of the object
print EndDevicesInner.to_json()

# convert the object into a dict
end_devices_inner_dict = end_devices_inner_instance.to_dict()
# create an instance of EndDevicesInner from a dict
end_devices_inner_form_dict = end_devices_inner.from_dict(end_devices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


