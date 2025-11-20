# src/patterns/strategy/coupon_discount.py
from .discount_strategy import DiscountStrategy

class CouponDiscount(DiscountStrategy):
    """
    Estratégia que valida um cupom e aplica o percentual associado.
    Caso o cupom não exista, aplica 0%.
    """

    def __init__(self, coupon_code: str):
        self.coupon_code = coupon_code
        self.valid_coupons = {
            "PROMO10": 10,
            "VIP20": 20,
            "FRETEGRATIS": 5,
        }

    def calculate_discount(self, amount: float) -> float:
        if self.coupon_code in self.valid_coupons:
            percent = self.valid_coupons[self.coupon_code]
            return amount * (percent / 100)
        return 0.0

