# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.service import Service


class UsagePoint(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    UsagePoint - a model defined in OpenAPI

        service: The service of this UsagePoint.
        usage_point_id: The usage_point_id of this UsagePoint.
        service_location_id: The service_location_id of this UsagePoint [Optional].
        substation_code_tm: The substation_code_tm of this UsagePoint.
        transformer_name: The transformer_name of this UsagePoint [Optional].
        bay_code_tm: The bay_code_tm of this UsagePoint [Optional].
        bay_name: The bay_name of this UsagePoint [Optional].
        line_code_tm: The line_code_tm of this UsagePoint [Optional].
        line_name: The line_name of this UsagePoint [Optional].
        tower_code_tm: The tower_code_tm of this UsagePoint [Optional].
        tower_name: The tower_name of this UsagePoint [Optional].
    """

    service: Service = Field(alias="Service")
    usage_point_id: str = Field(alias="UsagePointID")
    service_location_id: Optional[str] = Field(alias="ServiceLocationID", default=None)
    substation_code_tm: str = Field(alias="SubstationCodeTm")
    transformer_name: Optional[str] = Field(alias="TransformerName", default=None)
    bay_code_tm: Optional[str] = Field(alias="BayCodeTm", default=None)
    bay_name: Optional[str] = Field(alias="BayName", default=None)
    line_code_tm: Optional[str] = Field(alias="LineCodeTm", default=None)
    line_name: Optional[str] = Field(alias="LineName", default=None)
    tower_code_tm: Optional[str] = Field(alias="TowerCodeTm", default=None)
    tower_name: Optional[str] = Field(alias="TowerName", default=None)

UsagePoint.update_forward_refs()
