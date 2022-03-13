from __future__ import annotations
from typing import TYPE_CHECKING

from fastapi import FastAPI

from stella_api.core.utils.errors import FailureLoadVersion

if TYPE_CHECKING:
    from stella_api.core.models import RouteBase


__all__ = (
    'StellaAPI',
)


class StellaAPI(FastAPI):
    def __init__(self):
        super().__init__(title="Stella API")

    def create_route(self, router: RouteBase):
        try:
            router.setup()
            self.include_router(router.router, prefix=router.prefix)
        except Exception:
            raise FailureLoadVersion(router.prefix)
