from application.interfaces.repositories import SubscriptionRepository
from domain.subscriptions.entities import Subscription, SubscriptionType


class CreateSubscriptionUseCase:
    def __init__(self, subscription_repository: SubscriptionRepository):
        self.subscription_repository = subscription_repository

    def execute(self, id: int, user_id: int, plan: SubscriptionType) -> Subscription:
        new_subscription = Subscription(id=id, user_id=user_id, plan=plan)

        return self.subscription_repository.create(new_subscription)


class DeleteSubscriptionUseCase:
    def __init__(self, subscription_repository: SubscriptionRepository):
        self.subscription_repository = subscription_repository

    def execute(self, subscription_id: int):
        subscription = self.subscription_repository.find_by_id(subscription_id)
        if not subscription:
            raise Exception("Subscription not found")

        self.subscription_repository.delete(subscription_id)
