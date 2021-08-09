from fastapi import APIRouter

from app.common.models import SimpleMessageResponse

router = APIRouter()


@router.get("/", response_model=SimpleMessageResponse)
async def home():
    return {"message": "Visit /docs for OpenAPI Specs"}


# For K8 Healthiness probe
@router.get("/healthz", response_model=SimpleMessageResponse)
async def healthz():
    return {"message": "OK"}
