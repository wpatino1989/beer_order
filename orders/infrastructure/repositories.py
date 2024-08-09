from orders.domain.repositories import OrderRepository, StockRepository
from orders.domain.models import Order, OrderItem, OrderRound

class JsonOrderRepository(OrderRepository):
    def get_order_status(self) -> Order:
        return Order(
            created="2024-09-10 12:00:00",
            paid=False,
            subtotal=0,
            taxes=0,
            discounts=0,
            items=[],
            rounds=[
                OrderRound(
                    created="2024-09-10 12:00:30",
                    items=[
                        OrderItem(name="Corona", quantity=2, price_per_unit=115, total=230),
                        OrderItem(name="Club Colombia", quantity=1, price_per_unit=110, total=110),
                    ]
                ),
                OrderRound(
                    created="2024-09-10 12:20:31",
                    items=[
                        OrderItem(name="Club Colombia", quantity=1, price_per_unit=110, total=110),
                        OrderItem(name="Quilmes", quantity=2, price_per_unit=120, total=240),
                    ]
                ),
                OrderRound(
                    created="2024-09-10 12:43:21",
                    items=[
                        OrderItem(name="Quilmes", quantity=3, price_per_unit=120, total=360),
                    ]
                ),
            ]
        )

class JsonStockRepository(StockRepository):
    def get_stock(self) -> dict:
        return {
            "last_updated": "2024-09-10 12:00:00",
            "beers": [
                {"name": "Corona", "price": 115, "quantity": 2},
                {"name": "Quilmes", "price": 120, "quantity": 0},
                {"name": "Club Colombia", "price": 110, "quantity": 3}
            ]
        }
