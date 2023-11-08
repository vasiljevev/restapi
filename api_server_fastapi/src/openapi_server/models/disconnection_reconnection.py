# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.disconnection_reconnection_disconnection_list_inner import DisconnectionReconnectionDisconnectionListInner
from openapi_server.models.disconnection_reconnection_reconnection_list_inner import DisconnectionReconnectionReconnectionListInner


class DisconnectionReconnection(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    DisconnectionReconnection - a model defined in OpenAPI

        disconnection_list: The disconnection_list of this DisconnectionReconnection [Optional].
        reconnection_list: The reconnection_list of this DisconnectionReconnection [Optional].
    """

    disconnection_list: Optional[List[DisconnectionReconnectionDisconnectionListInner]] = Field(alias="DisconnectionList", default=None)
    reconnection_list: Optional[List[DisconnectionReconnectionReconnectionListInner]] = Field(alias="ReconnectionList", default=None)

DisconnectionReconnection.update_forward_refs()