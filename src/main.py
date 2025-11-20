from patterns.strategy.percentage_discount import PercentageDiscount
from patterns.strategy.shopping_cart import ShoppingCart
from patterns.facade.checkout_facade import CheckoutFacade


def main():
    print("\n===== SIMULAÇÃO DO E-COMMERCE =====\n")

    # 1. Criar o carrinho com uma estratégia de desconto
    cart = ShoppingCart(
        amount=350.00,
        discount_strategy=PercentageDiscount(10)  # 10%
    )

    # 2. Executar checkout pela facade
    checkout = CheckoutFacade()
    order = checkout.checkout(cart, order_id="ORDER-001")

    print("\n===== FINALIZADO =====\n")


if __name__ == "__main__":
    main()
