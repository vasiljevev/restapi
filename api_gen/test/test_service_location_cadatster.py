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

from openapi_client.models.service_location_cadatster import ServiceLocationCadatster  # noqa: E501

class TestServiceLocationCadatster(unittest.TestCase):
    """ServiceLocationCadatster unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceLocationCadatster:
        """Test ServiceLocationCadatster
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceLocationCadatster`
        """
        model = ServiceLocationCadatster()  # noqa: E501
        if include_optional:
            return ServiceLocationCadatster(
                cadaster = '77:232423443:14'
            )
        else:
            return ServiceLocationCadatster(
        )
        """

    def testServiceLocationCadatster(self):
        """Test ServiceLocationCadatster"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
