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

class EndDeviceRequestBodyParams(BaseModel):
    """
    EndDeviceRequestBodyParams
    """
    consumption_type: Optional[StrictStr] = Field(None, alias="ConsumptionType", description="Вид учета (flow - технический, estim - коммерческий)")
    device_type: Optional[conlist(StrictStr)] = Field(None, alias="DeviceType")
    date_begin: Optional[date] = Field(None, alias="Date_begin", description="Начальная дата анализа данных по потребителям")
    date_end: Optional[date] = Field(None, alias="Date_end", description="Начальная дата анализа данных по потребителям")
    usage_point_id: Optional[conlist(StrictStr)] = Field(None, alias="UsagePointID", description="Массив идентификаторов точек поставки")
    device_id_id: Optional[conlist(StrictStr)] = Field(None, alias="DeviceIdID", description="Массив идентификаторов приборов учета")
    system_state: Optional[conlist(StrictStr)] = Field(None, alias="SystemState")
    __properties = ["ConsumptionType", "DeviceType", "Date_begin", "Date_end", "UsagePointID", "DeviceIdID", "SystemState"]

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
    def from_json(cls, json_str: str) -> EndDeviceRequestBodyParams:
        """Create an instance of EndDeviceRequestBodyParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EndDeviceRequestBodyParams:
        """Create an instance of EndDeviceRequestBodyParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EndDeviceRequestBodyParams.parse_obj(obj)

        _obj = EndDeviceRequestBodyParams.parse_obj({
            "consumption_type": obj.get("ConsumptionType"),
            "device_type": obj.get("DeviceType"),
            "date_begin": obj.get("Date_begin"),
            "date_end": obj.get("Date_end"),
            "usage_point_id": obj.get("UsagePointID"),
            "device_id_id": obj.get("DeviceIdID"),
            "system_state": obj.get("SystemState")
        })
        return _obj


