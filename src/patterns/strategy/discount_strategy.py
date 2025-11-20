from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    """
    Interface base para todas as estratégias de desconto.
    Cada estratégia deve implementar o método calculate_discount().
    """

    @abstractmethod
    def calculate_discount(self, amount: float) -> float:
        pass

