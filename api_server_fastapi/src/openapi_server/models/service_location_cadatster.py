# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class ServiceLocationCadatster(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ServiceLocationCadatster - a model defined in OpenAPI

        cadaster: The cadaster of this ServiceLocationCadatster [Optional].
    """

    cadaster: Optional[str] = Field(alias="Cadaster", default=None)

ServiceLocationCadatster.update_forward_refs()