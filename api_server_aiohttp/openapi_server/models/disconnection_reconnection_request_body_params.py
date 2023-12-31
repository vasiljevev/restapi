# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class DisconnectionReconnectionRequestBodyParams(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, date_begin: date=None, date_end: date=None):
        """DisconnectionReconnectionRequestBodyParams - a model defined in OpenAPI

        :param date_begin: The date_begin of this DisconnectionReconnectionRequestBodyParams.
        :param date_end: The date_end of this DisconnectionReconnectionRequestBodyParams.
        """
        self.openapi_types = {
            'date_begin': date,
            'date_end': date
        }

        self.attribute_map = {
            'date_begin': 'Date_begin',
            'date_end': 'Date_end'
        }

        self._date_begin = date_begin
        self._date_end = date_end

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DisconnectionReconnectionRequestBodyParams':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Disconnection_Reconnection_request_body_Params of this DisconnectionReconnectionRequestBodyParams.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def date_begin(self):
        """Gets the date_begin of this DisconnectionReconnectionRequestBodyParams.

        Начальная дата анализа данных по потребителям

        :return: The date_begin of this DisconnectionReconnectionRequestBodyParams.
        :rtype: date
        """
        return self._date_begin

    @date_begin.setter
    def date_begin(self, date_begin):
        """Sets the date_begin of this DisconnectionReconnectionRequestBodyParams.

        Начальная дата анализа данных по потребителям

        :param date_begin: The date_begin of this DisconnectionReconnectionRequestBodyParams.
        :type date_begin: date
        """
        if date_begin is None:
            raise ValueError("Invalid value for `date_begin`, must not be `None`")

        self._date_begin = date_begin

    @property
    def date_end(self):
        """Gets the date_end of this DisconnectionReconnectionRequestBodyParams.

        Начальная дата анализа данных по потребителям

        :return: The date_end of this DisconnectionReconnectionRequestBodyParams.
        :rtype: date
        """
        return self._date_end

    @date_end.setter
    def date_end(self, date_end):
        """Sets the date_end of this DisconnectionReconnectionRequestBodyParams.

        Начальная дата анализа данных по потребителям

        :param date_end: The date_end of this DisconnectionReconnectionRequestBodyParams.
        :type date_end: date
        """
        if date_end is None:
            raise ValueError("Invalid value for `date_end`, must not be `None`")

        self._date_end = date_end
