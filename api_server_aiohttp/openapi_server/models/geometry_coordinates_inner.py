# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GeometryCoordinatesInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, x: float=None, y: float=None):
        """GeometryCoordinatesInner - a model defined in OpenAPI

        :param x: The x of this GeometryCoordinatesInner.
        :param y: The y of this GeometryCoordinatesInner.
        """
        self.openapi_types = {
            'x': float,
            'y': float
        }

        self.attribute_map = {
            'x': 'X',
            'y': 'Y'
        }

        self._x = x
        self._y = y

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GeometryCoordinatesInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Geometry_Coordinates_inner of this GeometryCoordinatesInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def x(self):
        """Gets the x of this GeometryCoordinatesInner.


        :return: The x of this GeometryCoordinatesInner.
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this GeometryCoordinatesInner.


        :param x: The x of this GeometryCoordinatesInner.
        :type x: float
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this GeometryCoordinatesInner.


        :return: The y of this GeometryCoordinatesInner.
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this GeometryCoordinatesInner.


        :param y: The y of this GeometryCoordinatesInner.
        :type y: float
        """

        self._y = y
