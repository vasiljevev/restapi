# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api_server_fastapi.src.openapi_server.apis.astu_api_base import BaseAstuApi
import api_server_fastapi.src.openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from api_server_fastapi.src.openapi_server.models.extra_models import TokenModel  # noqa: F401
from api_server_fastapi.src.openapi_server.models.consumers_inner import ConsumersInner
from api_server_fastapi.src.openapi_server.models.end_device_request_body import EndDeviceRequestBody
from api_server_fastapi.src.openapi_server.models.service_location import ServiceLocation


router = APIRouter()

ns_pkg = api_server_fastapi.src.openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/astu/import",
    responses={
        200: {"model": List[ConsumersInner], "description": "результаты поиска по запросу - определяются проектным решением для каждого сервиса индивидуально"},
        400: {"description": "не верные параметры сервиса или объекта запроса"},
        429: {"description": "АСТУ сформировало запросов больше чем описано в требованиях"},
        204: {"description": "витрину с данными не заполена или изменений нет"},
        408: {"description": "JSON формируется больше 1  мин"},
        500: {"description": "Server Error"},
        409: {"description": "Conflict"},
        404: {"description": "Not Found"},
        401: {"description": "Unauthorized"},
    },
    tags=["astu"],
    summary="Отправка объектов на обработку",
    response_model_by_alias=True,
)
async def process_objects(
    service_location: ServiceLocation = Body(None, description="Параметры обращения к сервису - определяются проектным решением для каждого сервиса индивидуально"),
) -> List[ConsumersInner]:
    """Отправка объектов на обработку"""
    return BaseAstuApi.subclasses[0]().process_objects(service_location)


@router.post(
    "/astu/export",
    responses={
        200: {"model": List[ConsumersInner], "description": "результаты поиска по запросу - определяются проектным решением для каждого сервиса индивидуально"},
        400: {"description": "не верные параметры сервиса или объекта запроса"},
        429: {"description": "АСТУ сформировало запросов больше чем описано в требованиях"},
        204: {"description": "витрину с данными не заполена или изменений нет"},
        408: {"description": "JSON формируется больше 1  мин"},
        500: {"description": "Server Error"},
        409: {"description": "Conflict"},
        404: {"description": "Not Found"},
        401: {"description": "Unauthorized"},
    },
    tags=["astu"],
    summary="Запрос поиска объектов",
    response_model_by_alias=True,
)
async def search_objects(
    end_device_request_body: EndDeviceRequestBody = Body(None, description="Параметры обращения к сервису - определяются проектным решением для каждого сервиса индивидуально"),
    limit: int = Query(None, description="кол-во элементов от начала отсчета", ge=0),
    offset: int = Query(None, description="индекс начала отчета", ge=0),
) -> List[ConsumersInner]:
    """Запрос поиска объектов по заданному сервису"""
    return BaseAstuApi.subclasses[0]().search_objects(end_device_request_body, limit, offset)
