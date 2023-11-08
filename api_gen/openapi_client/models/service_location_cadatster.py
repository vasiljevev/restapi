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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class ServiceLocationCadatster(BaseModel):
    """
    ServiceLocationCadatster
    """
    cadaster: Optional[StrictStr] = Field(None, alias="Cadaster", description="Кадастровый номер")
    __properties = ["Cadaster"]

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
    def from_json(cls, json_str: str) -> ServiceLocationCadatster:
        """Create an instance of ServiceLocationCadatster from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ServiceLocationCadatster:
        """Create an instance of ServiceLocationCadatster from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ServiceLocationCadatster.parse_obj(obj)

        _obj = ServiceLocationCadatster.parse_obj({
            "cadaster": obj.get("Cadaster")
        })
        return _obj


