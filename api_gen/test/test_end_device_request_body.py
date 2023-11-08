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

from openapi_client.models.end_device_request_body import EndDeviceRequestBody  # noqa: E501

class TestEndDeviceRequestBody(unittest.TestCase):
    """EndDeviceRequestBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EndDeviceRequestBody:
        """Test EndDeviceRequestBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EndDeviceRequestBody`
        """
        model = EndDeviceRequestBody()  # noqa: E501
        if include_optional:
            return EndDeviceRequestBody(
                service = openapi_client.models.service.Service(
                    service_type = 'Disconnection_Reconnection_list', 
                    filial = '23', 
                    area = [
                        '23'
                        ], ),
                params = openapi_client.models.end_device_request_body_params.EndDevice_request_body_Params(
                    consumption_type = 'flow', 
                    device_type = [
                        '1'
                        ], 
                    date_begin = 'Wed Mar 01 03:00:00 MSK 2023', 
                    date_end = 'Wed Mar 01 03:00:00 MSK 2023', 
                    usage_point_id = [
                        '22222222'
                        ], 
                    device_id_id = [
                        '10000012'
                        ], 
                    system_state = [
                        'Действующий, Проект'
                        ], )
            )
        else:
            return EndDeviceRequestBody(
                service = openapi_client.models.service.Service(
                    service_type = 'Disconnection_Reconnection_list', 
                    filial = '23', 
                    area = [
                        '23'
                        ], ),
                params = openapi_client.models.end_device_request_body_params.EndDevice_request_body_Params(
                    consumption_type = 'flow', 
                    device_type = [
                        '1'
                        ], 
                    date_begin = 'Wed Mar 01 03:00:00 MSK 2023', 
                    date_end = 'Wed Mar 01 03:00:00 MSK 2023', 
                    usage_point_id = [
                        '22222222'
                        ], 
                    device_id_id = [
                        '10000012'
                        ], 
                    system_state = [
                        'Действующий, Проект'
                        ], ),
        )
        """

    def testEndDeviceRequestBody(self):
        """Test EndDeviceRequestBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()