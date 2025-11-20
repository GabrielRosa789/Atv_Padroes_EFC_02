from .discount_strategy import DiscountStrategy

class ShoppingCart:
    """
    Carrinho que usa uma estratégia de desconto.
    """

    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy

    def set_discount_strategy(self, strategy: DiscountStrategy):
        """
        Permite trocar a estratégia dinamicamente.
        """
        self.discount_strategy = strategy

    def calculate_total(self, amount: float) -> float:
        """
        Calcula o valor total aplicando a estratégia atual.
        """
        discount = self.discount_strategy.calculate_discount(amount)
        total = amount - discount
        return total

