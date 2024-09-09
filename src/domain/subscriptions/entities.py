from enum import Enum
from dataclasses import dataclass

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
