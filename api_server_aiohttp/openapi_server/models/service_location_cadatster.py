# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ServiceLocationCadatster(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cadaster: str=None):
        """ServiceLocationCadatster - a model defined in OpenAPI

        :param cadaster: The cadaster of this ServiceLocationCadatster.
        """
        self.openapi_types = {
            'cadaster': str
        }

        self.attribute_map = {
            'cadaster': 'Cadaster'
        }

        self._cadaster = cadaster

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ServiceLocationCadatster':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ServiceLocation_Cadatster of this ServiceLocationCadatster.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cadaster(self):
        """Gets the cadaster of this ServiceLocationCadatster.

        Кадастровый номер

        :return: The cadaster of this ServiceLocationCadatster.
        :rtype: str
        """
        return self._cadaster

    @cadaster.setter
    def cadaster(self, cadaster):
        """Sets the cadaster of this ServiceLocationCadatster.

        Кадастровый номер

        :param cadaster: The cadaster of this ServiceLocationCadatster.
        :type cadaster: str
        """

        self._cadaster = cadaster
