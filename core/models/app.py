from fastapi import FastAPI
import asyncpg


class StellaAPI(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(title="Stella API", *args, **kwargs)
        self.pool = None
        self.user = kwargs.pop("db_user")
        self.password = kwargs.pop("db_pass")
        self.database_name = kwargs.pop("db_name")

    async def startup(self):
        self.pool = await asyncpg.create_pool(user=self.user, password=self.password, database=self.database_name)

    async def shutdown(self):
        self.pool.close()