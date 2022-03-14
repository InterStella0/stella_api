"""Just testing other file"""

from typing import Any, Dict

import pydantic

from fastapi import APIRouter

__all__ = ("router",)


class PingResponseModel(pydantic.BaseModel):
    message: str


router = APIRouter()


@router.get("", response_model=PingResponseModel)
async def get_ping() -> Dict[str, Any]:
    return {"message": "pong"}
