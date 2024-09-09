import typing as t

from domain.subscriptions.entities import Subscription
from application.interfaces.repositories import SubscriptionRepository


class InMemorySubscriptionRepository(SubscriptionRepository):
    def __init__(self):
        self.subscriptions = {}

    def create(self, subscription: Subscription) -> Subscription:
        self.subscriptions[subscription.id] = subscription
        return subscription

    def find_by_id(self, subscription_id: int) -> t.Optional[Subscription]:
        return self.subscriptions.get(subscription_id)
