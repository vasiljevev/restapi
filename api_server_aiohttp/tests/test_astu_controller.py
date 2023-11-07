# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.consumers_inner import ConsumersInner
from openapi_server.models.end_device_request_body import EndDeviceRequestBody
from openapi_server.models.service_location import ServiceLocation


async def test_process_objects(client):
    """Test case for process_objects

    Отправка объектов на обработку
    """
    body = {"Geometry":{"Type":"Point","Coordinates":[{"X":0.8008281904610115,"Y":6.027456183070403},{"X":0.8008281904610115,"Y":6.027456183070403}]},"Address":{"Address":"обл Московская , р-н Истринский, г Истра, д.1","Region":"Московская обл.","Street":"ул. Усадебная","House":"д.1","City":"г. Истра","District":"Истринский р-н"},"ServiceLocationId":"1233443","ConsumerId":"4564566","Service":{"Area":["23","23"],"ServiceType":"Disconnection_Reconnection_list","Filial":"23"},"Cadatster":{"Cadaster":"77:232423443:14"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/astu/import',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_search_objects(client):
    """Test case for search_objects

    Запрос поиска объектов
    """
    body = openapi_server.EndDeviceRequestBody()
    params = [('limit', 0),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/astu/export',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

