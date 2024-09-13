import typing as t

from application.interfaces.repositories import SubscriptionRepository
from domain.subscriptions.entities import Subscription


class InMemorySubscriptionRepository(SubscriptionRepository):
    def __init__(self):
        self.subscriptions = {}

    def create(self, subscription: Subscription) -> Subscription:
        self.subscriptions[subscription.id] = subscription
        return subscription

    def find_by_id(self, subscription_id: int) -> t.Optional[Subscription]:
        return self.subscriptions.get(subscription_id)

    def delete(self, subscription_id: int):
        if subscription_id in self.subscriptions:
            del self.subscriptions[subscription_id]
        else:
            raise Exception("Subscription not found")
