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


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist

class Service(BaseModel):
    """
    Service
    """
    service_type: StrictStr = Field(..., alias="ServiceType", description="Имя запрашиваемого сервиса Consumers, Disconnection_Reconnection_list, или EndDevices")
    filial: StrictStr = Field(..., alias="Filial", description="Идентификатор филиала из справочника КИС Баланс")
    area: conlist(StrictStr) = Field(..., alias="Area")
    __properties = ["ServiceType", "Filial", "Area"]

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
    def from_json(cls, json_str: str) -> Service:
        """Create an instance of Service from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Service:
        """Create an instance of Service from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Service.parse_obj(obj)

        _obj = Service.parse_obj({
            "service_type": obj.get("ServiceType"),
            "filial": obj.get("Filial"),
            "area": obj.get("Area")
        })
        return _obj


