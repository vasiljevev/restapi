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

from openapi_client.models.geometry_coordinates_inner import GeometryCoordinatesInner  # noqa: E501

class TestGeometryCoordinatesInner(unittest.TestCase):
    """GeometryCoordinatesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GeometryCoordinatesInner:
        """Test GeometryCoordinatesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GeometryCoordinatesInner`
        """
        model = GeometryCoordinatesInner()  # noqa: E501
        if include_optional:
            return GeometryCoordinatesInner(
                x = 1.337,
                y = 1.337
            )
        else:
            return GeometryCoordinatesInner(
        )
        """

    def testGeometryCoordinatesInner(self):
        """Test GeometryCoordinatesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()