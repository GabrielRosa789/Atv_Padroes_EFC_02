from .discount_strategy import DiscountStrategy

class ShoppingCart:
    """
    Carrinho que usa uma estratégia de desconto.
    """

    def __init__(self, amount: float, discount_strategy: DiscountStrategy):
        self.amount = amount
        self.discount_strategy = discount_strategy

    def set_discount_strategy(self, strategy: DiscountStrategy):
        self.discount_strategy = strategy

    def calculate_total(self, amount: float = None) -> float:
        """
        Calcula o valor total aplicando a estratégia atual.
        """
        amount = amount if amount is not None else self.amount
        discount = self.discount_strategy.calculate_discount(amount)
        return amount - discount
