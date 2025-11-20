from .discount_strategy import DiscountStrategy

class ProgressiveDiscount(DiscountStrategy):
    """
    Estratégia de desconto progressivo:
    """

    def calculate_discount(self, amount: float) -> float:
        if amount > 500:
            return amount * 0.15
        elif amount > 100:
            return amount * 0.10
        else:
            return amount * 0.05

