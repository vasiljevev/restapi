# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class Service(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Service - a model defined in OpenAPI

        service_type: The service_type of this Service.
        filial: The filial of this Service.
        area: The area of this Service.
    """

    service_type: str = Field(alias="ServiceType")
    filial: str = Field(alias="Filial")
    area: List[str] = Field(alias="Area")

Service.update_forward_refs()