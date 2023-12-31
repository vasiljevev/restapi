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

from openapi_client.models.consumers_inner import ConsumersInner  # noqa: E501

class TestConsumersInner(unittest.TestCase):
    """ConsumersInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConsumersInner:
        """Test ConsumersInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConsumersInner`
        """
        model = ConsumersInner()  # noqa: E501
        if include_optional:
            return ConsumersInner(
                action_type = 'INSERT',
                consumer_id = '345435345',
                consumer_name = 'Голованова Надежда Фёдоровна',
                consumer_type = 'ФЛ',
                contract = '10-132344',
                requets_number = 'МС/103/13234234/12',
                service_location_id = '23244322',
                name = 'обл Московская , р-н Истринский, г Истра, д.1',
                organization_id = '2308',
                object_status = 'Действующий',
                fias_id = 'b749c3e6-39df-45ae-918f-a5e6c8abb54e',
                address = 'обл Московская , р-н Истринский, г Истра, д.1',
                region = 'Московская обл.',
                district = 'Истринский р-н',
                city = 'г. Истра',
                street = 'ул. Усадебная',
                house = 'д.1',
                room = 'кв. 47',
                remark = 'Примечание к адресу',
                cadaster = '23:12323:11',
                max_power = '0.23',
                reliability_category = '3',
                phone = '89629991999',
                residents_count = '12',
                service_disp_category = 'Частный дом',
                num_of_storeys = '2',
                stand_by_capacity = '0',
                significance = '33',
                service_contingency_catagory = 'Непроизводственные потребители',
                in_charge_full_name = 'Иванов И.И.',
                emergency_power_reserve = '0.22',
                techno_power_reserve = '265',
                techno_power_reserve_duration = 'number',
                geometry = openapi_client.models.geometry.Geometry(
                    type = 'Point', 
                    coordinates = [
                        openapi_client.models.geometry_coordinates_inner.Geometry_Coordinates_inner(
                            x = 1.337, 
                            y = 1.337, )
                        ], ),
                usage_points = [
                    openapi_client.models.consumers_inner_usage_points_inner.Consumers_inner_UsagePoints_inner(
                        action_type = 'INSERT', 
                        usage_point_id = '1233455', 
                        name = 'Описание точки поставки', 
                        organization_id = '2308', 
                        is_sdp = True, 
                        voltage_level = 'НН', 
                        voltage_class = '0.4', 
                        service_location_id = '1233443', 
                        substation_code_tm = 'TP010-00032333', 
                        substation_name = 'ТП 3004', 
                        transformer_name = 'Т-1', 
                        bay_code_tm = 'TP010-00032333-16-01-01', 
                        bay_name = 'яч. 1 ф. ВЛ 0,4 кВ', 
                        line_code_tm = 'VN004-00003234', 
                        line_name = 'ВЛ 0,4 кВ 1', 
                        tower_code_tm = 'VN004-00003234-001-1001', 
                        tower_name = 'Опора 1', 
                        remark = 'На кабельных наконечниках отходящего фидера 0,4 кВ ф. 1 ТП-3004', 
                        geometry = openapi_client.models.geometry.Geometry(
                            type = 'Point', 
                            coordinates = [
                                openapi_client.models.geometry_coordinates_inner.Geometry_Coordinates_inner(
                                    x = 1.337, 
                                    y = 1.337, )
                                ], ), )
                    ]
            )
        else:
            return ConsumersInner(
        )
        """

    def testConsumersInner(self):
        """Test ConsumersInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
