# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.geometry import Geometry


class DisconnectionReconnectionDisconnectionListInnerUsagePointsInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    DisconnectionReconnectionDisconnectionListInnerUsagePointsInner - a model defined in OpenAPI

        action_type: The action_type of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner [Optional].
        name: The name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner [Optional].
        organization_id: The organization_id of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner [Optional].
        is_sdp: The is_sdp of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner [Optional].
        voltage_level: The voltage_level of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner [Optional].
        voltage_class: The voltage_class of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner [Optional].
        service_location_id: The service_location_id of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner [Optional].
        substation_code_tm: The substation_code_tm of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner [Optional].
        substation_name: The substation_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner [Optional].
        transformer_name: The transformer_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner [Optional].
        bay_code_tm: The bay_code_tm of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner [Optional].
        bay_name: The bay_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner [Optional].
        line_code_tm: The line_code_tm of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner [Optional].
        line_name: The line_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner [Optional].
        tower_code_tm: The tower_code_tm of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner [Optional].
        tower_name: The tower_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner [Optional].
        remark: The remark of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner [Optional].
        geometry: The geometry of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner [Optional].
    """

    action_type: Optional[str] = Field(alias="ActionType", default=None)
    name: Optional[str] = Field(alias="Name", default=None)
    organization_id: Optional[str] = Field(alias="OrganizationID", default=None)
    is_sdp: Optional[str] = Field(alias="IsSDP", default=None)
    voltage_level: Optional[str] = Field(alias="VoltageLevel", default=None)
    voltage_class: Optional[str] = Field(alias="VoltageClass", default=None)
    service_location_id: Optional[str] = Field(alias="ServiceLocationID", default=None)
    substation_code_tm: Optional[str] = Field(alias="SubstationCodeTm", default=None)
    substation_name: Optional[str] = Field(alias="SubstationName", default=None)
    transformer_name: Optional[str] = Field(alias="TransformerName", default=None)
    bay_code_tm: Optional[str] = Field(alias="BayCodeTm", default=None)
    bay_name: Optional[str] = Field(alias="BayName", default=None)
    line_code_tm: Optional[str] = Field(alias="LineCodeTm", default=None)
    line_name: Optional[str] = Field(alias="LineName", default=None)
    tower_code_tm: Optional[str] = Field(alias="TowerCodeTm", default=None)
    tower_name: Optional[str] = Field(alias="TowerName", default=None)
    remark: Optional[str] = Field(alias="Remark", default=None)
    geometry: Optional[Geometry] = Field(alias="geometry", default=None)

DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.update_forward_refs()
