from asyncio import AbstractEventLoop, get_event_loop
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config.settings import settings
from app.routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # start up
    yield
    # shut down


app: FastAPI = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
    dependencies=[],
)

app.include_router(router)

if __name__ == "__main__":
    loop: AbstractEventLoop = get_event_loop()
    loop.run_forever()
