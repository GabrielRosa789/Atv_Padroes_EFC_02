from abc import ABC, abstractmethod


class Product(ABC):
    """
    Classe base para produtos do sistema.
    """

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @abstractmethod
    def get_description(self) -> str:
        pass


class Book(Product):
    """
    Produto: Livro
    """

    def get_description(self) -> str:
        return f"[Livro] {self.name} - R$ {self.price:.2f}"


class Electronics(Product):
    """
    Produto: Eletrônico
    """

    def get_description(self) -> str:
        return f"[Eletrônico] {self.name} - R$ {self.price:.2f}"


class Clothing(Product):
    """
    Produto: Vestuário
    """

    def get_description(self) -> str:
        return f"[Vestuário] {self.name} - R$ {self.price:.2f}"

