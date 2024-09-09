from domain.subscriptions.entities import Subscription, SubscriptionType
from application.interfaces.repositories import SubscriptionRepository


class CreateSubscriptionUseCase:
    def __init__(self, subscription_repository: SubscriptionRepository):
        self.subscription_repository = subscription_repository

    def execute(self, id: int, user_id: int, plan: SubscriptionType) -> Subscription:
        new_subscription = Subscription(id=id, user_id=user_id, plan=plan)

        return self.subscription_repository.create(new_subscription)
