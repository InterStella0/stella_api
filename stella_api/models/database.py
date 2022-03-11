import asyncpg

from stella_api.settings import settings


class Database:
    async def startup(self) -> None:
        self.pool = await asyncpg.create_pool(
            host=settings.POSTGRES_HOST,
            user=settings.POSTGRES_USER,
            password=settings.POSTGRES_PASSWORD,
            database=settings.POSTGRES_DATABASE,
        )

    async def shutdown(self) -> None:
        self.pool.close()