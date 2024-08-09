from dataclasses import dataclass, asdict
from typing import List

@dataclass
class Beer:
    name: str
    price: int
    quantity: int

    def to_dict(self):
        return asdict(self)

@dataclass
class OrderItem:
    name: str
    quantity: int
    price_per_unit: int
    total: int

    def to_dict(self):
        return asdict(self)

@dataclass
class OrderRound:
    created: str
    items: List[OrderItem]

    def to_dict(self):
        return asdict(self)

@dataclass
class Order:
    created: str
    paid: bool
    subtotal: int
    taxes: int
    discounts: int
    items: List[OrderItem]
    rounds: List[OrderRound]

    def to_dict(self):
        return asdict(self)