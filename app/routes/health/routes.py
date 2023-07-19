from fastapi import APIRouter

from app.services.health.models import Health
from app.services.health.health import health

router = APIRouter()

@router.get("/health", response_model=Health)
async def heart_ckeck_route() -> Health:
  return health()