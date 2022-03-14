from typing import Any

from fastapi import APIRouter

__all__ = ("RouteBase",)


class RouteBase:
    def __init__(self, prefix: str) -> None:
        self.prefix = prefix
        self.router = APIRouter()

    def add_router(self, router: APIRouter, *args: Any, **kwargs: Any) -> None:
        self.router.include_router(router, *args, **kwargs)

    def setup(self) -> None:
        raise NotImplementedError()

    @property
    def description(self) -> str:
        return self.__doc__ or ""
