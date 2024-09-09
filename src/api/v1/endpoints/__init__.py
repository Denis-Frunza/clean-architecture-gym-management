from fastapi import APIRouter

from .subscriptions import subscriptions


router = APIRouter()

router.include_router(subscriptions.router)
