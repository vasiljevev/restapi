# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ConsumersRequestBodyParams(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type: str=None, date_begin: date=None, date_end: date=None, consumer_id: List[str]=None, service_location_id: List[str]=None, system_state: List[str]=None):
        """ConsumersRequestBodyParams - a model defined in OpenAPI

        :param type: The type of this ConsumersRequestBodyParams.
        :param date_begin: The date_begin of this ConsumersRequestBodyParams.
        :param date_end: The date_end of this ConsumersRequestBodyParams.
        :param consumer_id: The consumer_id of this ConsumersRequestBodyParams.
        :param service_location_id: The service_location_id of this ConsumersRequestBodyParams.
        :param system_state: The system_state of this ConsumersRequestBodyParams.
        """
        self.openapi_types = {
            'type': str,
            'date_begin': date,
            'date_end': date,
            'consumer_id': List[str],
            'service_location_id': List[str],
            'system_state': List[str]
        }

        self.attribute_map = {
            'type': 'type',
            'date_begin': 'Date_begin',
            'date_end': 'Date_end',
            'consumer_id': 'ConsumerID',
            'service_location_id': 'ServiceLocationID',
            'system_state': 'SystemState'
        }

        self._type = type
        self._date_begin = date_begin
        self._date_end = date_end
        self._consumer_id = consumer_id
        self._service_location_id = service_location_id
        self._system_state = system_state

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ConsumersRequestBodyParams':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Consumers_request_body_Params of this ConsumersRequestBodyParams.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this ConsumersRequestBodyParams.

        Тип потребителя (ФЛ, ЮЛ) из справочника КИС Баланс

        :return: The type of this ConsumersRequestBodyParams.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConsumersRequestBodyParams.

        Тип потребителя (ФЛ, ЮЛ) из справочника КИС Баланс

        :param type: The type of this ConsumersRequestBodyParams.
        :type type: str
        """

        self._type = type

    @property
    def date_begin(self):
        """Gets the date_begin of this ConsumersRequestBodyParams.

        Начальная дата анализа данных по потребителям

        :return: The date_begin of this ConsumersRequestBodyParams.
        :rtype: date
        """
        return self._date_begin

    @date_begin.setter
    def date_begin(self, date_begin):
        """Sets the date_begin of this ConsumersRequestBodyParams.

        Начальная дата анализа данных по потребителям

        :param date_begin: The date_begin of this ConsumersRequestBodyParams.
        :type date_begin: date
        """

        self._date_begin = date_begin

    @property
    def date_end(self):
        """Gets the date_end of this ConsumersRequestBodyParams.

        Конечная дата анализа данных по потребителям

        :return: The date_end of this ConsumersRequestBodyParams.
        :rtype: date
        """
        return self._date_end

    @date_end.setter
    def date_end(self, date_end):
        """Sets the date_end of this ConsumersRequestBodyParams.

        Конечная дата анализа данных по потребителям

        :param date_end: The date_end of this ConsumersRequestBodyParams.
        :type date_end: date
        """

        self._date_end = date_end

    @property
    def consumer_id(self):
        """Gets the consumer_id of this ConsumersRequestBodyParams.


        :return: The consumer_id of this ConsumersRequestBodyParams.
        :rtype: List[str]
        """
        return self._consumer_id

    @consumer_id.setter
    def consumer_id(self, consumer_id):
        """Sets the consumer_id of this ConsumersRequestBodyParams.


        :param consumer_id: The consumer_id of this ConsumersRequestBodyParams.
        :type consumer_id: List[str]
        """

        self._consumer_id = consumer_id

    @property
    def service_location_id(self):
        """Gets the service_location_id of this ConsumersRequestBodyParams.


        :return: The service_location_id of this ConsumersRequestBodyParams.
        :rtype: List[str]
        """
        return self._service_location_id

    @service_location_id.setter
    def service_location_id(self, service_location_id):
        """Sets the service_location_id of this ConsumersRequestBodyParams.


        :param service_location_id: The service_location_id of this ConsumersRequestBodyParams.
        :type service_location_id: List[str]
        """

        self._service_location_id = service_location_id

    @property
    def system_state(self):
        """Gets the system_state of this ConsumersRequestBodyParams.


        :return: The system_state of this ConsumersRequestBodyParams.
        :rtype: List[str]
        """
        return self._system_state

    @system_state.setter
    def system_state(self, system_state):
        """Sets the system_state of this ConsumersRequestBodyParams.


        :param system_state: The system_state of this ConsumersRequestBodyParams.
        :type system_state: List[str]
        """

        self._system_state = system_state
