"""File layout test"""

from typing import Any, Dict

import pydantic

from fastapi import APIRouter

__all__ = ("router",)


class PPMeterModel(pydantic.BaseModel):
    message: str


router = APIRouter()


@router.get("/pp", response_model=PPMeterModel)
async def get_pp(lasted: int = 5) -> Dict[str, Any]:
    return {"message": f"around {lasted}"}
