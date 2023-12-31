# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class EndDeviceRequestBodyParams(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, consumption_type: str=None, device_type: List[str]=None, date_begin: date=None, date_end: date=None, usage_point_id: List[str]=None, device_id_id: List[str]=None, system_state: List[str]=None):
        """EndDeviceRequestBodyParams - a model defined in OpenAPI

        :param consumption_type: The consumption_type of this EndDeviceRequestBodyParams.
        :param device_type: The device_type of this EndDeviceRequestBodyParams.
        :param date_begin: The date_begin of this EndDeviceRequestBodyParams.
        :param date_end: The date_end of this EndDeviceRequestBodyParams.
        :param usage_point_id: The usage_point_id of this EndDeviceRequestBodyParams.
        :param device_id_id: The device_id_id of this EndDeviceRequestBodyParams.
        :param system_state: The system_state of this EndDeviceRequestBodyParams.
        """
        self.openapi_types = {
            'consumption_type': str,
            'device_type': List[str],
            'date_begin': date,
            'date_end': date,
            'usage_point_id': List[str],
            'device_id_id': List[str],
            'system_state': List[str]
        }

        self.attribute_map = {
            'consumption_type': 'ConsumptionType',
            'device_type': 'DeviceType',
            'date_begin': 'Date_begin',
            'date_end': 'Date_end',
            'usage_point_id': 'UsagePointID',
            'device_id_id': 'DeviceIdID',
            'system_state': 'SystemState'
        }

        self._consumption_type = consumption_type
        self._device_type = device_type
        self._date_begin = date_begin
        self._date_end = date_end
        self._usage_point_id = usage_point_id
        self._device_id_id = device_id_id
        self._system_state = system_state

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EndDeviceRequestBodyParams':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The EndDevice_request_body_Params of this EndDeviceRequestBodyParams.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def consumption_type(self):
        """Gets the consumption_type of this EndDeviceRequestBodyParams.

        Вид учета (flow - технический, estim - коммерческий)

        :return: The consumption_type of this EndDeviceRequestBodyParams.
        :rtype: str
        """
        return self._consumption_type

    @consumption_type.setter
    def consumption_type(self, consumption_type):
        """Sets the consumption_type of this EndDeviceRequestBodyParams.

        Вид учета (flow - технический, estim - коммерческий)

        :param consumption_type: The consumption_type of this EndDeviceRequestBodyParams.
        :type consumption_type: str
        """

        self._consumption_type = consumption_type

    @property
    def device_type(self):
        """Gets the device_type of this EndDeviceRequestBodyParams.


        :return: The device_type of this EndDeviceRequestBodyParams.
        :rtype: List[str]
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this EndDeviceRequestBodyParams.


        :param device_type: The device_type of this EndDeviceRequestBodyParams.
        :type device_type: List[str]
        """

        self._device_type = device_type

    @property
    def date_begin(self):
        """Gets the date_begin of this EndDeviceRequestBodyParams.

        Начальная дата анализа данных по потребителям

        :return: The date_begin of this EndDeviceRequestBodyParams.
        :rtype: date
        """
        return self._date_begin

    @date_begin.setter
    def date_begin(self, date_begin):
        """Sets the date_begin of this EndDeviceRequestBodyParams.

        Начальная дата анализа данных по потребителям

        :param date_begin: The date_begin of this EndDeviceRequestBodyParams.
        :type date_begin: date
        """

        self._date_begin = date_begin

    @property
    def date_end(self):
        """Gets the date_end of this EndDeviceRequestBodyParams.

        Начальная дата анализа данных по потребителям

        :return: The date_end of this EndDeviceRequestBodyParams.
        :rtype: date
        """
        return self._date_end

    @date_end.setter
    def date_end(self, date_end):
        """Sets the date_end of this EndDeviceRequestBodyParams.

        Начальная дата анализа данных по потребителям

        :param date_end: The date_end of this EndDeviceRequestBodyParams.
        :type date_end: date
        """

        self._date_end = date_end

    @property
    def usage_point_id(self):
        """Gets the usage_point_id of this EndDeviceRequestBodyParams.

        Массив идентификаторов точек поставки

        :return: The usage_point_id of this EndDeviceRequestBodyParams.
        :rtype: List[str]
        """
        return self._usage_point_id

    @usage_point_id.setter
    def usage_point_id(self, usage_point_id):
        """Sets the usage_point_id of this EndDeviceRequestBodyParams.

        Массив идентификаторов точек поставки

        :param usage_point_id: The usage_point_id of this EndDeviceRequestBodyParams.
        :type usage_point_id: List[str]
        """

        self._usage_point_id = usage_point_id

    @property
    def device_id_id(self):
        """Gets the device_id_id of this EndDeviceRequestBodyParams.

        Массив идентификаторов приборов учета

        :return: The device_id_id of this EndDeviceRequestBodyParams.
        :rtype: List[str]
        """
        return self._device_id_id

    @device_id_id.setter
    def device_id_id(self, device_id_id):
        """Sets the device_id_id of this EndDeviceRequestBodyParams.

        Массив идентификаторов приборов учета

        :param device_id_id: The device_id_id of this EndDeviceRequestBodyParams.
        :type device_id_id: List[str]
        """

        self._device_id_id = device_id_id

    @property
    def system_state(self):
        """Gets the system_state of this EndDeviceRequestBodyParams.


        :return: The system_state of this EndDeviceRequestBodyParams.
        :rtype: List[str]
        """
        return self._system_state

    @system_state.setter
    def system_state(self, system_state):
        """Sets the system_state of this EndDeviceRequestBodyParams.


        :param system_state: The system_state of this EndDeviceRequestBodyParams.
        :type system_state: List[str]
        """

        self._system_state = system_state
