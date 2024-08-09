from orders.domain.repositories import OrderRepository, StockRepository
from orders.domain.models import Order

class OrderService:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def get_order_status(self) -> Order:
        return self.order_repository.get_order_status()

class StockService:
    def __init__(self, stock_repository: StockRepository):
        self.stock_repository = stock_repository

    def get_stock(self) -> dict:
        return self.stock_repository.get_stock()
