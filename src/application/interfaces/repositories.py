import typing as t

from abc import ABC, abstractmethod
from domain.subscriptions.entities import Subscription


class SubscriptionRepository(ABC):
    @abstractmethod
    def create(self, subscription: Subscription) -> Subscription:
        ...

    @abstractmethod
    def find_by_id(self, subscription_id: int) -> t.Optional[Subscription]:
        ...
