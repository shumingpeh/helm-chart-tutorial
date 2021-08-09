from fastapi import FastAPI

from app.addition_math import router as addition
from app.addition_math.store import app_store
from app.common.router import router as common_router

app = FastAPI()

app.include_router(common_router, prefix="", tags=["Core"])
app.include_router(addition.router, prefix="/v1", tags=["Addition Model"])


@app.on_event("startup")
async def startup() -> None:
    app_store.load()

    app_store.http_client.start()
