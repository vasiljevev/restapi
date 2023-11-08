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

from openapi_client.models.disconnection_reconnection_request_body import DisconnectionReconnectionRequestBody  # noqa: E501

class TestDisconnectionReconnectionRequestBody(unittest.TestCase):
    """DisconnectionReconnectionRequestBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DisconnectionReconnectionRequestBody:
        """Test DisconnectionReconnectionRequestBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DisconnectionReconnectionRequestBody`
        """
        model = DisconnectionReconnectionRequestBody()  # noqa: E501
        if include_optional:
            return DisconnectionReconnectionRequestBody(
                service = openapi_client.models.service.Service(
                    service_type = 'Disconnection_Reconnection_list', 
                    filial = '23', 
                    area = [
                        '23'
                        ], ),
                params = openapi_client.models.disconnection_reconnection_request_body_params.Disconnection_Reconnection_request_body_Params(
                    date_begin = 'Wed Mar 01 03:00:00 MSK 2023', 
                    date_end = 'Wed Mar 01 03:00:00 MSK 2023', )
            )
        else:
            return DisconnectionReconnectionRequestBody(
                service = openapi_client.models.service.Service(
                    service_type = 'Disconnection_Reconnection_list', 
                    filial = '23', 
                    area = [
                        '23'
                        ], ),
                params = openapi_client.models.disconnection_reconnection_request_body_params.Disconnection_Reconnection_request_body_Params(
                    date_begin = 'Wed Mar 01 03:00:00 MSK 2023', 
                    date_end = 'Wed Mar 01 03:00:00 MSK 2023', ),
        )
        """

    def testDisconnectionReconnectionRequestBody(self):
        """Test DisconnectionReconnectionRequestBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
