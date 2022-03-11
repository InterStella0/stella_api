from fastapi import APIRouter

from . import funny

__all__ = ("router",)

router = APIRouter()
router.include_router(funny.router, prefix="/funny", tags=["funny"])
