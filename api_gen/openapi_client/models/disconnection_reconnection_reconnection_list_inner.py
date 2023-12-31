# coding: utf-8

"""
    Omnuis-API astu specificatioin

    Интеграционный сервис АИС КИС Баланс

    The version of the OpenAPI document: 2.0
    Contact: e-vasilyev@it-serv.ru
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from openapi_client.models.disconnection_reconnection_disconnection_list_inner_usage_points_inner import DisconnectionReconnectionDisconnectionListInnerUsagePointsInner

class DisconnectionReconnectionReconnectionListInner(BaseModel):
    """
    DisconnectionReconnectionReconnectionListInner
    """
    action_type: Optional[StrictStr] = Field(None, alias="ActionType")
    reconnection_id: Optional[StrictStr] = Field(None, alias="ReconnectionId")
    discconection_id: Optional[StrictStr] = Field(None, alias="DiscconectionId")
    description: Optional[StrictStr] = Field(None, alias="Description")
    type: Optional[StrictStr] = Field(None, alias="Type")
    reason: Optional[StrictStr] = Field(None, alias="Reason")
    var_date: Optional[date] = Field(None, alias="Date")
    area: Optional[StrictStr] = Field(None, alias="Area")
    initiator: Optional[StrictStr] = Field(None, alias="Initiator")
    performer: Optional[StrictStr] = Field(None, alias="Performer")
    consumer_id: Optional[StrictStr] = Field(None, alias="ConsumerId")
    usage_points: Optional[conlist(DisconnectionReconnectionDisconnectionListInnerUsagePointsInner)] = Field(None, alias="UsagePoints")
    __properties = ["ActionType", "ReconnectionId", "DiscconectionId", "Description", "Type", "Reason", "Date", "Area", "Initiator", "Performer", "ConsumerId", "UsagePoints"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> DisconnectionReconnectionReconnectionListInner:
        """Create an instance of DisconnectionReconnectionReconnectionListInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in usage_points (list)
        _items = []
        if self.usage_points:
            for _item in self.usage_points:
                if _item:
                    _items.append(_item.to_dict())
            _dict['UsagePoints'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DisconnectionReconnectionReconnectionListInner:
        """Create an instance of DisconnectionReconnectionReconnectionListInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DisconnectionReconnectionReconnectionListInner.parse_obj(obj)

        _obj = DisconnectionReconnectionReconnectionListInner.parse_obj({
            "action_type": obj.get("ActionType"),
            "reconnection_id": obj.get("ReconnectionId"),
            "discconection_id": obj.get("DiscconectionId"),
            "description": obj.get("Description"),
            "type": obj.get("Type"),
            "reason": obj.get("Reason"),
            "var_date": obj.get("Date"),
            "area": obj.get("Area"),
            "initiator": obj.get("Initiator"),
            "performer": obj.get("Performer"),
            "consumer_id": obj.get("ConsumerId"),
            "usage_points": [DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.from_dict(_item) for _item in obj.get("UsagePoints")] if obj.get("UsagePoints") is not None else None
        })
        return _obj


