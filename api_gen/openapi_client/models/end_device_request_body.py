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



from pydantic import BaseModel, Field
from openapi_client.models.end_device_request_body_params import EndDeviceRequestBodyParams
from openapi_client.models.service import Service

class EndDeviceRequestBody(BaseModel):
    """
    5.1 Параметры тела запроса для сервиса EndDevice  # noqa: E501
    """
    service: Service = Field(..., alias="Service")
    params: EndDeviceRequestBodyParams = Field(..., alias="Params")
    __properties = ["Service", "Params"]

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
    def from_json(cls, json_str: str) -> EndDeviceRequestBody:
        """Create an instance of EndDeviceRequestBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of service
        if self.service:
            _dict['Service'] = self.service.to_dict()
        # override the default output from pydantic by calling `to_dict()` of params
        if self.params:
            _dict['Params'] = self.params.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EndDeviceRequestBody:
        """Create an instance of EndDeviceRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EndDeviceRequestBody.parse_obj(obj)

        _obj = EndDeviceRequestBody.parse_obj({
            "service": Service.from_dict(obj.get("Service")) if obj.get("Service") is not None else None,
            "params": EndDeviceRequestBodyParams.from_dict(obj.get("Params")) if obj.get("Params") is not None else None
        })
        return _obj


