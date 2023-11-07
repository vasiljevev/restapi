# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.geometry import Geometry
from openapi_server import util


class DisconnectionReconnectionDisconnectionListInnerUsagePointsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, action_type: str=None, name: str=None, organization_id: str=None, is_sdp: str=None, voltage_level: str=None, voltage_class: str=None, service_location_id: str=None, substation_code_tm: str=None, substation_name: str=None, transformer_name: str=None, bay_code_tm: str=None, bay_name: str=None, line_code_tm: str=None, line_name: str=None, tower_code_tm: str=None, tower_name: str=None, remark: str=None, geometry: Geometry=None):
        """DisconnectionReconnectionDisconnectionListInnerUsagePointsInner - a model defined in OpenAPI

        :param action_type: The action_type of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :param name: The name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :param organization_id: The organization_id of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :param is_sdp: The is_sdp of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :param voltage_level: The voltage_level of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :param voltage_class: The voltage_class of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :param service_location_id: The service_location_id of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :param substation_code_tm: The substation_code_tm of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :param substation_name: The substation_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :param transformer_name: The transformer_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :param bay_code_tm: The bay_code_tm of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :param bay_name: The bay_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :param line_code_tm: The line_code_tm of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :param line_name: The line_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :param tower_code_tm: The tower_code_tm of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :param tower_name: The tower_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :param remark: The remark of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :param geometry: The geometry of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        """
        self.openapi_types = {
            'action_type': str,
            'name': str,
            'organization_id': str,
            'is_sdp': str,
            'voltage_level': str,
            'voltage_class': str,
            'service_location_id': str,
            'substation_code_tm': str,
            'substation_name': str,
            'transformer_name': str,
            'bay_code_tm': str,
            'bay_name': str,
            'line_code_tm': str,
            'line_name': str,
            'tower_code_tm': str,
            'tower_name': str,
            'remark': str,
            'geometry': Geometry
        }

        self.attribute_map = {
            'action_type': 'ActionType',
            'name': 'Name',
            'organization_id': 'OrganizationID',
            'is_sdp': 'IsSDP',
            'voltage_level': 'VoltageLevel',
            'voltage_class': 'VoltageClass',
            'service_location_id': 'ServiceLocationID',
            'substation_code_tm': 'SubstationCodeTm',
            'substation_name': 'SubstationName',
            'transformer_name': 'TransformerName',
            'bay_code_tm': 'BayCodeTm',
            'bay_name': 'BayName',
            'line_code_tm': 'LineCodeTm',
            'line_name': 'LineName',
            'tower_code_tm': 'TowerCodeTm',
            'tower_name': 'TowerName',
            'remark': 'Remark',
            'geometry': 'geometry'
        }

        self._action_type = action_type
        self._name = name
        self._organization_id = organization_id
        self._is_sdp = is_sdp
        self._voltage_level = voltage_level
        self._voltage_class = voltage_class
        self._service_location_id = service_location_id
        self._substation_code_tm = substation_code_tm
        self._substation_name = substation_name
        self._transformer_name = transformer_name
        self._bay_code_tm = bay_code_tm
        self._bay_name = bay_name
        self._line_code_tm = line_code_tm
        self._line_name = line_name
        self._tower_code_tm = tower_code_tm
        self._tower_name = tower_name
        self._remark = remark
        self._geometry = geometry

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DisconnectionReconnectionDisconnectionListInnerUsagePointsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Disconnection_Reconnection_DisconnectionList_inner_UsagePoints_inner of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def action_type(self):
        """Gets the action_type of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :return: The action_type of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :param action_type: The action_type of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :type action_type: str
        """

        self._action_type = action_type

    @property
    def name(self):
        """Gets the name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :return: The name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :param name: The name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :type name: str
        """

        self._name = name

    @property
    def organization_id(self):
        """Gets the organization_id of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :return: The organization_id of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :param organization_id: The organization_id of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :type organization_id: str
        """

        self._organization_id = organization_id

    @property
    def is_sdp(self):
        """Gets the is_sdp of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :return: The is_sdp of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :rtype: str
        """
        return self._is_sdp

    @is_sdp.setter
    def is_sdp(self, is_sdp):
        """Sets the is_sdp of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :param is_sdp: The is_sdp of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :type is_sdp: str
        """

        self._is_sdp = is_sdp

    @property
    def voltage_level(self):
        """Gets the voltage_level of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :return: The voltage_level of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :rtype: str
        """
        return self._voltage_level

    @voltage_level.setter
    def voltage_level(self, voltage_level):
        """Sets the voltage_level of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :param voltage_level: The voltage_level of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :type voltage_level: str
        """

        self._voltage_level = voltage_level

    @property
    def voltage_class(self):
        """Gets the voltage_class of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :return: The voltage_class of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :rtype: str
        """
        return self._voltage_class

    @voltage_class.setter
    def voltage_class(self, voltage_class):
        """Sets the voltage_class of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :param voltage_class: The voltage_class of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :type voltage_class: str
        """

        self._voltage_class = voltage_class

    @property
    def service_location_id(self):
        """Gets the service_location_id of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :return: The service_location_id of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :rtype: str
        """
        return self._service_location_id

    @service_location_id.setter
    def service_location_id(self, service_location_id):
        """Sets the service_location_id of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :param service_location_id: The service_location_id of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :type service_location_id: str
        """

        self._service_location_id = service_location_id

    @property
    def substation_code_tm(self):
        """Gets the substation_code_tm of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :return: The substation_code_tm of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :rtype: str
        """
        return self._substation_code_tm

    @substation_code_tm.setter
    def substation_code_tm(self, substation_code_tm):
        """Sets the substation_code_tm of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :param substation_code_tm: The substation_code_tm of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :type substation_code_tm: str
        """

        self._substation_code_tm = substation_code_tm

    @property
    def substation_name(self):
        """Gets the substation_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :return: The substation_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :rtype: str
        """
        return self._substation_name

    @substation_name.setter
    def substation_name(self, substation_name):
        """Sets the substation_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :param substation_name: The substation_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :type substation_name: str
        """

        self._substation_name = substation_name

    @property
    def transformer_name(self):
        """Gets the transformer_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :return: The transformer_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :rtype: str
        """
        return self._transformer_name

    @transformer_name.setter
    def transformer_name(self, transformer_name):
        """Sets the transformer_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :param transformer_name: The transformer_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :type transformer_name: str
        """

        self._transformer_name = transformer_name

    @property
    def bay_code_tm(self):
        """Gets the bay_code_tm of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :return: The bay_code_tm of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :rtype: str
        """
        return self._bay_code_tm

    @bay_code_tm.setter
    def bay_code_tm(self, bay_code_tm):
        """Sets the bay_code_tm of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :param bay_code_tm: The bay_code_tm of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :type bay_code_tm: str
        """

        self._bay_code_tm = bay_code_tm

    @property
    def bay_name(self):
        """Gets the bay_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :return: The bay_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :rtype: str
        """
        return self._bay_name

    @bay_name.setter
    def bay_name(self, bay_name):
        """Sets the bay_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :param bay_name: The bay_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :type bay_name: str
        """

        self._bay_name = bay_name

    @property
    def line_code_tm(self):
        """Gets the line_code_tm of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :return: The line_code_tm of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :rtype: str
        """
        return self._line_code_tm

    @line_code_tm.setter
    def line_code_tm(self, line_code_tm):
        """Sets the line_code_tm of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :param line_code_tm: The line_code_tm of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :type line_code_tm: str
        """

        self._line_code_tm = line_code_tm

    @property
    def line_name(self):
        """Gets the line_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :return: The line_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :rtype: str
        """
        return self._line_name

    @line_name.setter
    def line_name(self, line_name):
        """Sets the line_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :param line_name: The line_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :type line_name: str
        """

        self._line_name = line_name

    @property
    def tower_code_tm(self):
        """Gets the tower_code_tm of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :return: The tower_code_tm of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :rtype: str
        """
        return self._tower_code_tm

    @tower_code_tm.setter
    def tower_code_tm(self, tower_code_tm):
        """Sets the tower_code_tm of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :param tower_code_tm: The tower_code_tm of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :type tower_code_tm: str
        """

        self._tower_code_tm = tower_code_tm

    @property
    def tower_name(self):
        """Gets the tower_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :return: The tower_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :rtype: str
        """
        return self._tower_name

    @tower_name.setter
    def tower_name(self, tower_name):
        """Sets the tower_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :param tower_name: The tower_name of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :type tower_name: str
        """

        self._tower_name = tower_name

    @property
    def remark(self):
        """Gets the remark of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :return: The remark of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :param remark: The remark of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :type remark: str
        """

        self._remark = remark

    @property
    def geometry(self):
        """Gets the geometry of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :return: The geometry of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :rtype: Geometry
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.


        :param geometry: The geometry of this DisconnectionReconnectionDisconnectionListInnerUsagePointsInner.
        :type geometry: Geometry
        """

        self._geometry = geometry
