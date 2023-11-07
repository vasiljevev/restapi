# DisconnectionReconnectionReconnectionListInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | **str** |  | [optional] 
**reconnection_id** | **str** |  | [optional] 
**discconection_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**var_date** | **date** |  | [optional] 
**area** | **str** |  | [optional] 
**initiator** | **str** |  | [optional] 
**performer** | **str** |  | [optional] 
**consumer_id** | **str** |  | [optional] 
**usage_points** | [**List[DisconnectionReconnectionDisconnectionListInnerUsagePointsInner]**](DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.disconnection_reconnection_reconnection_list_inner import DisconnectionReconnectionReconnectionListInner

# TODO update the JSON string below
json = "{}"
# create an instance of DisconnectionReconnectionReconnectionListInner from a JSON string
disconnection_reconnection_reconnection_list_inner_instance = DisconnectionReconnectionReconnectionListInner.from_json(json)
# print the JSON string representation of the object
print DisconnectionReconnectionReconnectionListInner.to_json()

# convert the object into a dict
disconnection_reconnection_reconnection_list_inner_dict = disconnection_reconnection_reconnection_list_inner_instance.to_dict()
# create an instance of DisconnectionReconnectionReconnectionListInner from a dict
disconnection_reconnection_reconnection_list_inner_form_dict = disconnection_reconnection_reconnection_list_inner.from_dict(disconnection_reconnection_reconnection_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


