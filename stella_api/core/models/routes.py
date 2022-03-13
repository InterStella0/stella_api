from typing import Any, List
from fastapi import APIRouter

__all__ = (
    'RouteBase',
)


class RouteBase:
    def __init__(self, prefix) -> None:
        self.prefix: str = prefix
        self.router: APIRouter = APIRouter()
    
    def add_router(self, router: APIRouter, *args: Any, **kwargs: Any):
        self.router.include_router(router, *args, **kwargs)

    def setup(self) -> None:
        raise NotImplemented()

    @property
    def description(self):
        return self.__doc__

