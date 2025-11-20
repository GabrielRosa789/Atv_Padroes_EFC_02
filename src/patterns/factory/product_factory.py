from .product import Book, Electronics, Clothing, Product


class ProductFactory:
    """
    Fábrica responsável por criar produtos a partir de dados.
    """

    @staticmethod
    def create_product(category: str, name: str, price: float) -> Product:
        """
        Método fábrica.
        Retorna uma instância da classe correta conforme a categoria.
        """

        category = category.lower()

        if category == "book":
            return Book(name, price)

        elif category == "electronics":
            return Electronics(name, price)

        elif category == "clothing":
            return Clothing(name, price)

        else:
            raise ValueError(f"Categoria de produto desconhecida: {category}")

