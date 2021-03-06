from stella_api.core.models.routes import RouteBase

from . import funny, ping

__all__ = ("V0Route",)


class V0Route(RouteBase):
    """The pre-release wahtever API"""

    def __init__(self) -> None:
        super().__init__("/v0")

    def setup(self) -> None:
        self.add_router(funny.router, prefix="/funny", tags=["funny"])
        self.add_router(ping.router, prefix="/ping", tags=["misc"])
