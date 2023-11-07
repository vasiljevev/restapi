# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.consumers_inner import ConsumersInner
from openapi_server.models.end_device_request_body import EndDeviceRequestBody
from openapi_server.models.service_location import ServiceLocation


class BaseAstuApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseAstuApi.subclasses = BaseAstuApi.subclasses + (cls,)
    def process_objects(
        self,
        service_location: ServiceLocation,
    ) -> List[ConsumersInner]:
        """Отправка объектов на обработку"""
        ...


    def search_objects(
        self,
        end_device_request_body: EndDeviceRequestBody,
        limit: int,
        offset: int,
    ) -> List[ConsumersInner]:
        """Запрос поиска объектов по заданному сервису"""
        ...
