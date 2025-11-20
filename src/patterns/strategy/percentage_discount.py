from .discount_strategy import DiscountStrategy

class PercentageDiscount(DiscountStrategy):
    """
    Estratégia que aplica um desconto percentual sobre o valor total.
    """

    def __init__(self, percent: float):
        self.percent = percent

    def calculate_discount(self, amount: float) -> float:
        return amount * (self.percent / 100)

