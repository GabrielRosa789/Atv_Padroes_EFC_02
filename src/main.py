# src/main.py
from patterns.strategy.shopping_cart import ShoppingCart
from patterns.strategy.percentage_discount import PercentageDiscount
from patterns.strategy.fixed_discount import FixedDiscount
from patterns.strategy.progressive_discount import ProgressiveDiscount
from patterns.strategy.coupon_discount import CouponDiscount

if __name__ == "__main__":
    amount = 350

    cart = ShoppingCart(PercentageDiscount(10))
    print("Percentual:", cart.calculate_total(amount))

    cart.set_discount_strategy(FixedDiscount(50))
    print("Fixo:", cart.calculate_total(amount))

    cart.set_discount_strategy(ProgressiveDiscount())
    print("Progressivo:", cart.calculate_total(amount))

    cart.set_discount_strategy(CouponDiscount("VIP20"))
    print("Cupom:", cart.calculate_total(amount))

