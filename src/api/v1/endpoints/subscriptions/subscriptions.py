from dataclasses import asdict
from fastapi import APIRouter, HTTPException


from api.v1.endpoints.subscriptions.model import CreateSubscriptionRequest, SubscriptionResponse
from application.services.subscription_service import SubscriptionService
from infrastructure.repositories.subscription_repository import InMemorySubscriptionRepository

router = APIRouter()

subscription_repository = InMemorySubscriptionRepository()

subscription_service = SubscriptionService(subscription_repository)


@router.post("/subscriptions/", response_model=SubscriptionResponse)
def create_subscription(subscription_request: CreateSubscriptionRequest):
    try:
        new_subscription = subscription_service.create_subscription(
            id=subscription_request.id,
            user_id=subscription_request.user_id,
            plan=subscription_request.plan
        )
        return SubscriptionResponse(**asdict(new_subscription))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
