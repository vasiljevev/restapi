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

from openapi_client.models.end_devices_inner import EndDevicesInner  # noqa: E501

class TestEndDevicesInner(unittest.TestCase):
    """EndDevicesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EndDevicesInner:
        """Test EndDevicesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EndDevicesInner`
        """
        model = EndDevicesInner()  # noqa: E501
        if include_optional:
            return EndDevicesInner(
                action_type = 'string',
                end_device_id = 'string',
                name = 'string',
                organization_id = 'string',
                device_type = 'string',
                serial_number = 'string',
                is_amr = 'boolean',
                is_commercial = 'boolean',
                device_status = 'string',
                belonging_type = 'string',
                usage_point_id = 'string',
                substation_code_tm = 'string',
                bay_code_tm = 'string',
                line_code_tm = 'string',
                tower_code_tm = 'string',
                device_location = 'string',
                geometry = openapi_client.models.geometry.Geometry(
                    type = 'Point', 
                    coordinates = [
                        openapi_client.models.geometry_coordinates_inner.Geometry_Coordinates_inner(
                            x = 1.337, 
                            y = 1.337, )
                        ], ),
                measure_points = [
                    openapi_client.models.end_devices_inner_measure_points_inner.EndDevices_inner_MeasurePoints_inner(
                        id = 'string', 
                        description = 'string', 
                        type = 'string', )
                    ]
            )
        else:
            return EndDevicesInner(
        )
        """

    def testEndDevicesInner(self):
        """Test EndDevicesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
