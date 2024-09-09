from application.use_cases.create_subscription import CreateSubscriptionUseCase
from domain.subscriptions.entities import Subscription, SubscriptionType
from infrastructure.repositories.subscription_repository import SubscriptionRepository


class SubscriptionService:
    def __init__(self, subscription_repository: SubscriptionRepository):

        self.subscription_repository = subscription_repository

    def create_subscription(self, id: int, user_id: int, plan: SubscriptionType) -> Subscription:

        create_subscription_use_case = CreateSubscriptionUseCase(self.subscription_repository)

        return create_subscription_use_case.execute(id=id, user_id=user_id, plan=plan)
