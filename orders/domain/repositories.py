from abc import ABC, abstractmethod
from .models import Order

class OrderRepository(ABC):
    @abstractmethod
    def get_order_status(self) -> Order:
        pass

class StockRepository(ABC):
    @abstractmethod
    def get_stock(self) -> dict:
        pass