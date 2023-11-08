# coding: utf-8

"""
    Omnuis-API astu specificatioin

    Интеграционный сервис АИС КИС Баланс

    The version of the OpenAPI document: 2.0
    Contact: e-vasilyev@it-serv.ru
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.disconnection_reconnection import DisconnectionReconnection  # noqa: E501

class TestDisconnectionReconnection(unittest.TestCase):
    """DisconnectionReconnection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DisconnectionReconnection:
        """Test DisconnectionReconnection
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DisconnectionReconnection`
        """
        model = DisconnectionReconnection()  # noqa: E501
        if include_optional:
            return DisconnectionReconnection(
                disconnection_list = [
                    openapi_client.models.disconnection_reconnection_disconnection_list_inner.Disconnection_Reconnection_DisconnectionList_inner(
                        action_type = 'string', 
                        discconection_id = 'string', 
                        description = 'string', 
                        type = 'string', 
                        reason = 'string', 
                        date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        area = 'string', 
                        initiator = 'string', 
                        performer = 'string', 
                        consumer_id = 'string', 
                        usage_points = [
                            openapi_client.models.disconnection_reconnection_disconnection_list_inner_usage_points_inner.Disconnection_Reconnection_DisconnectionList_inner_UsagePoints_inner(
                                action_type = 'string', 
                                name = 'string', 
                                organization_id = 'string', 
                                is_sdp = 'boolean', 
                                voltage_level = 'string', 
                                voltage_class = 'string', 
                                service_location_id = 'string', 
                                substation_code_tm = 'string', 
                                substation_name = 'string', 
                                transformer_name = 'string', 
                                bay_code_tm = 'string', 
                                bay_name = 'string', 
                                line_code_tm = 'string', 
                                line_name = 'string', 
                                tower_code_tm = 'string', 
                                tower_name = 'string', 
                                remark = 'string', 
                                geometry = openapi_client.models.geometry.Geometry(
                                    type = 'Point', 
                                    coordinates = [
                                        openapi_client.models.geometry_coordinates_inner.Geometry_Coordinates_inner(
                                            x = 1.337, 
                                            y = 1.337, )
                                        ], ), )
                            ], )
                    ],
                reconnection_list = [
                    openapi_client.models.disconnection_reconnection_reconnection_list_inner.Disconnection_Reconnection_ReconnectionList_inner(
                        action_type = 'string', 
                        reconnection_id = 'string', 
                        discconection_id = 'string', 
                        description = 'string', 
                        type = 'string', 
                        reason = 'string', 
                        date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        area = 'string', 
                        initiator = 'string', 
                        performer = 'string', 
                        consumer_id = 'string', 
                        usage_points = [
                            openapi_client.models.disconnection_reconnection_disconnection_list_inner_usage_points_inner.Disconnection_Reconnection_DisconnectionList_inner_UsagePoints_inner(
                                action_type = 'string', 
                                name = 'string', 
                                organization_id = 'string', 
                                is_sdp = 'boolean', 
                                voltage_level = 'string', 
                                voltage_class = 'string', 
                                service_location_id = 'string', 
                                substation_code_tm = 'string', 
                                substation_name = 'string', 
                                transformer_name = 'string', 
                                bay_code_tm = 'string', 
                                bay_name = 'string', 
                                line_code_tm = 'string', 
                                line_name = 'string', 
                                tower_code_tm = 'string', 
                                tower_name = 'string', 
                                remark = 'string', 
                                geometry = openapi_client.models.geometry.Geometry(
                                    type = 'Point', 
                                    coordinates = [
                                        openapi_client.models.geometry_coordinates_inner.Geometry_Coordinates_inner(
                                            x = 1.337, 
                                            y = 1.337, )
                                        ], ), )
                            ], )
                    ]
            )
        else:
            return DisconnectionReconnection(
        )
        """

    def testDisconnectionReconnection(self):
        """Test DisconnectionReconnection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
