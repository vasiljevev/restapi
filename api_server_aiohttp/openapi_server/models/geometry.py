# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.geometry_coordinates_inner import GeometryCoordinatesInner
from openapi_server import util


class Geometry(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type: str=None, coordinates: List[GeometryCoordinatesInner]=None):
        """Geometry - a model defined in OpenAPI

        :param type: The type of this Geometry.
        :param coordinates: The coordinates of this Geometry.
        """
        self.openapi_types = {
            'type': str,
            'coordinates': List[GeometryCoordinatesInner]
        }

        self.attribute_map = {
            'type': 'Type',
            'coordinates': 'Coordinates'
        }

        self._type = type
        self._coordinates = coordinates

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Geometry':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Geometry of this Geometry.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this Geometry.


        :return: The type of this Geometry.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Geometry.


        :param type: The type of this Geometry.
        :type type: str
        """

        self._type = type

    @property
    def coordinates(self):
        """Gets the coordinates of this Geometry.


        :return: The coordinates of this Geometry.
        :rtype: List[GeometryCoordinatesInner]
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this Geometry.


        :param coordinates: The coordinates of this Geometry.
        :type coordinates: List[GeometryCoordinatesInner]
        """

        self._coordinates = coordinates
