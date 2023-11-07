from typing import List, Dict
from aiohttp import web

from openapi_server.models.consumers_inner import ConsumersInner
from openapi_server.models.end_device_request_body import EndDeviceRequestBody
from openapi_server.models.service_location import ServiceLocation
from openapi_server import util


async def process_objects(request: web.Request, body) -> web.Response:
    """Отправка объектов на обработку

    Отправка объектов на обработку

    :param body: Параметры обращения к сервису - определяются проектным решением для каждого сервиса индивидуально
    :type body: dict | bytes

    """
    body = ServiceLocation.from_dict(body)
    return web.Response(status=200)


async def search_objects(request: web.Request, body, limit=None, offset=None) -> web.Response:
    """Запрос поиска объектов

    Запрос поиска объектов по заданному сервису

    :param body: Параметры обращения к сервису - определяются проектным решением для каждого сервиса индивидуально
    :type body: dict | bytes
    :param limit: кол-во элементов от начала отсчета
    :type limit: int
    :param offset: индекс начала отчета
    :type offset: int

    """
    body = EndDeviceRequestBody.from_dict(body)
    return web.Response(status=200)
