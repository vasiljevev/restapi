# DisconnectionReconnection

4.1 Сервис по запросу ПТК АСТУ возвращает из КИС Баланс данные о введенных ограничениях / возобновлении подачи ээ по указанным районам, созданные / измененные / удаленные за период Date_begin и Date_end

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disconnection_list** | [**List[DisconnectionReconnectionDisconnectionListInner]**](DisconnectionReconnectionDisconnectionListInner.md) | Массив данных по отключениям | [optional] 
**reconnection_list** | [**List[DisconnectionReconnectionReconnectionListInner]**](DisconnectionReconnectionReconnectionListInner.md) | Массив данных по возобновлению | [optional] 

## Example

```python
from openapi_client.models.disconnection_reconnection import DisconnectionReconnection

# TODO update the JSON string below
json = "{}"
# create an instance of DisconnectionReconnection from a JSON string
disconnection_reconnection_instance = DisconnectionReconnection.from_json(json)
# print the JSON string representation of the object
print DisconnectionReconnection.to_json()

# convert the object into a dict
disconnection_reconnection_dict = disconnection_reconnection_instance.to_dict()
# create an instance of DisconnectionReconnection from a dict
disconnection_reconnection_form_dict = disconnection_reconnection.from_dict(disconnection_reconnection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


