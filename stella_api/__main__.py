import logging
from stella_api.core.models import StellaAPI

import uvicorn

from .routes import setup_routes
from .settings import settings

log = logging.getLogger(__name__)

try:
    import uvloop
except ImportError:
    log.warning("uvloop not available")
else:
    uvloop.install()


def main() -> None:
    app = StellaAPI()
    setup_routes(app)

    uvicorn.run(
        app,
        host=settings.HOST,
        port=settings.PORT,
    )


if __name__ == "__main__":
    main()
