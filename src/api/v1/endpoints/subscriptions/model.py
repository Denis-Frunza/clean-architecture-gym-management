from enum import Enum

from pydantic import BaseModel


class SubscriptionType(str, Enum):
    free = "Free"
    starter = "Starter"
    pro = "Pro"


class CreateSubscriptionRequest(BaseModel):
    id: int
    user_id: int
    plan: SubscriptionType


class SubscriptionResponse(BaseModel):
    id: int
    user_id: int
    plan: SubscriptionType
    is_active: bool

    class Config:
        orm_mode = True
