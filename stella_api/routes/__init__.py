from fastapi import APIRouter, FastAPI

from . import v0

__all__ = ("setup_routes",)

router = APIRouter()
router.include_router(v0.router, prefix="/v0")


def setup_routes(app: FastAPI) -> None:
    app.include_router(router)
