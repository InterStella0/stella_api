from stella_api.core.models import StellaAPI
from stella_api.routes.v0 import V0Route


__all__ = ("setup_routes",)


def setup_routes(app: StellaAPI) -> None:
    app.create_route(V0Route())
