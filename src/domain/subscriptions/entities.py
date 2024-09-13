from dataclasses import dataclass
from enum import Enum


class SubscriptionType(str, Enum):
    free = "Free"
    starter = "Starter"
    pro = "Pro"


@dataclass
class Subscription:
    id: int
    user_id: int
    plan: SubscriptionType
    is_active: bool = True
