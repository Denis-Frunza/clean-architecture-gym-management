from abc import ABC, abstractmethod
import typing as t

from domain.subscriptions.entities import Subscription


class SubscriptionRepository(ABC):
    @abstractmethod
    def create(self, subscription: Subscription) -> Subscription: ...

    @abstractmethod
    def find_by_id(self, subscription_id: int) -> t.Optional[Subscription]: ...

    @abstractmethod
    def delete(self, subscription_id: int): ...
