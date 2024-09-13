from application.use_cases.create_subscription import CreateSubscriptionUseCase, DeleteSubscriptionUseCase
from domain.subscriptions.entities import Subscription, SubscriptionType
from infrastructure.repositories.subscription_repository import SubscriptionRepository


class SubscriptionService:
    def __init__(self, subscription_repository: SubscriptionRepository):

        self.subscription_repository = subscription_repository

    def create_subscription(
        self, id: int, user_id: int, plan: SubscriptionType
    ) -> Subscription:
        create_subscription_use_case = CreateSubscriptionUseCase(
            self.subscription_repository
        )
        return create_subscription_use_case.execute(id=id, user_id=user_id, plan=plan)

    def get_subscription(self, subscription_id: int) -> Subscription:
        subscription = self.subscription_repository.find_by_id(subscription_id)

        if not subscription:
            raise Exception("Subscription not found")
        return subscription

    def delete_subscription(self, subscription_id: int):
        delete_subscription_use_case = DeleteSubscriptionUseCase(
            self.subscription_repository
        )
        delete_subscription_use_case.execute(subscription_id)
