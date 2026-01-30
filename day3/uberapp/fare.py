
from __future__ import annotations

def calculate_fare(distance_km: int, **kwargs) -> float:
   
    base_fare = float(kwargs.get("base_fare", 40))
    per_km = float(kwargs.get("per_km", 12))
    surge = float(kwargs.get("surge", 1.0))
    discount = float(kwargs.get("discount", 0.0))

    amount = base_fare + (max(distance_km, 0) * per_km)
    amount = amount * max(surge, 0.0)
    amount = amount - max(discount, 0.0)
    return round(max(amount, 0.0), 2)
