# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.disconnection_reconnection_disconnection_list_inner_usage_points_inner import DisconnectionReconnectionDisconnectionListInnerUsagePointsInner
from openapi_server import util


class DisconnectionReconnectionDisconnectionListInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, action_type: str=None, discconection_id: str=None, description: str=None, type: str=None, reason: str=None, date: date=None, area: str=None, initiator: str=None, performer: str=None, consumer_id: str=None, usage_points: List[DisconnectionReconnectionDisconnectionListInnerUsagePointsInner]=None):
        """DisconnectionReconnectionDisconnectionListInner - a model defined in OpenAPI

        :param action_type: The action_type of this DisconnectionReconnectionDisconnectionListInner.
        :param discconection_id: The discconection_id of this DisconnectionReconnectionDisconnectionListInner.
        :param description: The description of this DisconnectionReconnectionDisconnectionListInner.
        :param type: The type of this DisconnectionReconnectionDisconnectionListInner.
        :param reason: The reason of this DisconnectionReconnectionDisconnectionListInner.
        :param date: The date of this DisconnectionReconnectionDisconnectionListInner.
        :param area: The area of this DisconnectionReconnectionDisconnectionListInner.
        :param initiator: The initiator of this DisconnectionReconnectionDisconnectionListInner.
        :param performer: The performer of this DisconnectionReconnectionDisconnectionListInner.
        :param consumer_id: The consumer_id of this DisconnectionReconnectionDisconnectionListInner.
        :param usage_points: The usage_points of this DisconnectionReconnectionDisconnectionListInner.
        """
        self.openapi_types = {
            'action_type': str,
            'discconection_id': str,
            'description': str,
            'type': str,
            'reason': str,
            'date': date,
            'area': str,
            'initiator': str,
            'performer': str,
            'consumer_id': str,
            'usage_points': List[DisconnectionReconnectionDisconnectionListInnerUsagePointsInner]
        }

        self.attribute_map = {
            'action_type': 'ActionType',
            'discconection_id': 'DiscconectionId',
            'description': 'Description',
            'type': 'Type',
            'reason': 'Reason',
            'date': 'Date',
            'area': 'Area',
            'initiator': 'Initiator',
            'performer': 'Performer',
            'consumer_id': 'ConsumerId',
            'usage_points': 'UsagePoints'
        }

        self._action_type = action_type
        self._discconection_id = discconection_id
        self._description = description
        self._type = type
        self._reason = reason
        self._date = date
        self._area = area
        self._initiator = initiator
        self._performer = performer
        self._consumer_id = consumer_id
        self._usage_points = usage_points

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DisconnectionReconnectionDisconnectionListInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Disconnection_Reconnection_DisconnectionList_inner of this DisconnectionReconnectionDisconnectionListInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def action_type(self):
        """Gets the action_type of this DisconnectionReconnectionDisconnectionListInner.


        :return: The action_type of this DisconnectionReconnectionDisconnectionListInner.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this DisconnectionReconnectionDisconnectionListInner.


        :param action_type: The action_type of this DisconnectionReconnectionDisconnectionListInner.
        :type action_type: str
        """

        self._action_type = action_type

    @property
    def discconection_id(self):
        """Gets the discconection_id of this DisconnectionReconnectionDisconnectionListInner.


        :return: The discconection_id of this DisconnectionReconnectionDisconnectionListInner.
        :rtype: str
        """
        return self._discconection_id

    @discconection_id.setter
    def discconection_id(self, discconection_id):
        """Sets the discconection_id of this DisconnectionReconnectionDisconnectionListInner.


        :param discconection_id: The discconection_id of this DisconnectionReconnectionDisconnectionListInner.
        :type discconection_id: str
        """

        self._discconection_id = discconection_id

    @property
    def description(self):
        """Gets the description of this DisconnectionReconnectionDisconnectionListInner.


        :return: The description of this DisconnectionReconnectionDisconnectionListInner.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DisconnectionReconnectionDisconnectionListInner.


        :param description: The description of this DisconnectionReconnectionDisconnectionListInner.
        :type description: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this DisconnectionReconnectionDisconnectionListInner.


        :return: The type of this DisconnectionReconnectionDisconnectionListInner.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DisconnectionReconnectionDisconnectionListInner.


        :param type: The type of this DisconnectionReconnectionDisconnectionListInner.
        :type type: str
        """

        self._type = type

    @property
    def reason(self):
        """Gets the reason of this DisconnectionReconnectionDisconnectionListInner.


        :return: The reason of this DisconnectionReconnectionDisconnectionListInner.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this DisconnectionReconnectionDisconnectionListInner.


        :param reason: The reason of this DisconnectionReconnectionDisconnectionListInner.
        :type reason: str
        """

        self._reason = reason

    @property
    def date(self):
        """Gets the date of this DisconnectionReconnectionDisconnectionListInner.


        :return: The date of this DisconnectionReconnectionDisconnectionListInner.
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this DisconnectionReconnectionDisconnectionListInner.


        :param date: The date of this DisconnectionReconnectionDisconnectionListInner.
        :type date: date
        """

        self._date = date

    @property
    def area(self):
        """Gets the area of this DisconnectionReconnectionDisconnectionListInner.


        :return: The area of this DisconnectionReconnectionDisconnectionListInner.
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this DisconnectionReconnectionDisconnectionListInner.


        :param area: The area of this DisconnectionReconnectionDisconnectionListInner.
        :type area: str
        """

        self._area = area

    @property
    def initiator(self):
        """Gets the initiator of this DisconnectionReconnectionDisconnectionListInner.


        :return: The initiator of this DisconnectionReconnectionDisconnectionListInner.
        :rtype: str
        """
        return self._initiator

    @initiator.setter
    def initiator(self, initiator):
        """Sets the initiator of this DisconnectionReconnectionDisconnectionListInner.


        :param initiator: The initiator of this DisconnectionReconnectionDisconnectionListInner.
        :type initiator: str
        """

        self._initiator = initiator

    @property
    def performer(self):
        """Gets the performer of this DisconnectionReconnectionDisconnectionListInner.


        :return: The performer of this DisconnectionReconnectionDisconnectionListInner.
        :rtype: str
        """
        return self._performer

    @performer.setter
    def performer(self, performer):
        """Sets the performer of this DisconnectionReconnectionDisconnectionListInner.


        :param performer: The performer of this DisconnectionReconnectionDisconnectionListInner.
        :type performer: str
        """

        self._performer = performer

    @property
    def consumer_id(self):
        """Gets the consumer_id of this DisconnectionReconnectionDisconnectionListInner.


        :return: The consumer_id of this DisconnectionReconnectionDisconnectionListInner.
        :rtype: str
        """
        return self._consumer_id

    @consumer_id.setter
    def consumer_id(self, consumer_id):
        """Sets the consumer_id of this DisconnectionReconnectionDisconnectionListInner.


        :param consumer_id: The consumer_id of this DisconnectionReconnectionDisconnectionListInner.
        :type consumer_id: str
        """

        self._consumer_id = consumer_id

    @property
    def usage_points(self):
        """Gets the usage_points of this DisconnectionReconnectionDisconnectionListInner.


        :return: The usage_points of this DisconnectionReconnectionDisconnectionListInner.
        :rtype: List[DisconnectionReconnectionDisconnectionListInnerUsagePointsInner]
        """
        return self._usage_points

    @usage_points.setter
    def usage_points(self, usage_points):
        """Sets the usage_points of this DisconnectionReconnectionDisconnectionListInner.


        :param usage_points: The usage_points of this DisconnectionReconnectionDisconnectionListInner.
        :type usage_points: List[DisconnectionReconnectionDisconnectionListInnerUsagePointsInner]
        """

        self._usage_points = usage_points