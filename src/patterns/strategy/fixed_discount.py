# src/patterns/strategy/fixed_discount.py
from .discount_strategy import DiscountStrategy

class FixedDiscount(DiscountStrategy):
    """
    Estratégia que aplica um valor fixo de desconto.
    """

    def __init__(self, value: float):
        self.value = value

    def calculate_discount(self, amount: float) -> float:
        return min(self.value, amount)

