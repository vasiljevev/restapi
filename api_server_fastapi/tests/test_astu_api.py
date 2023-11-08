# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.consumers_inner import ConsumersInner  # noqa: F401
from openapi_server.models.end_device_request_body import EndDeviceRequestBody  # noqa: F401
from openapi_server.models.service_location import ServiceLocation  # noqa: F401


def test_process_objects(client: TestClient):
    """Test case for process_objects

    Отправка объектов на обработку
    """
    service_location = {"geometry":{"type":"Point","coordinates":[{"x":0.8008281904610115,"y":6.027456183070403},{"x":0.8008281904610115,"y":6.027456183070403}]},"address":{"address":"обл Московская , р-н Истринский, г Истра, д.1","region":"Московская обл.","street":"ул. Усадебная","house":"д.1","city":"г. Истра","district":"Истринский р-н"},"service_location_id":"1233443","consumer_id":"4564566","service":{"area":["23","23"],"service_type":"Disconnection_Reconnection_list","filial":"23"},"cadatster":{"cadaster":"77:232423443:14"}}

    headers = {
    }
    response = client.request(
        "POST",
        "/astu/import",
        headers=headers,
        json=service_location,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_search_objects(client: TestClient):
    """Test case for search_objects

    Запрос поиска объектов
    """
    end_device_request_body = openapi_server.EndDeviceRequestBody()
    params = [("limit", 0),     ("offset", 0)]
    headers = {
    }
    response = client.request(
        "POST",
        "/astu/export",
        headers=headers,
        json=end_device_request_body,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

