from dataclasses import dataclass, field

@dataclass(init=True)
class Motoboy:
    id: int
    exclusive_stores: list
    fare_price: float
    assigned_orders: list
    profit: float = 0.0
