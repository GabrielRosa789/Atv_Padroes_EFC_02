from patterns.strategy.shopping_cart import ShoppingCart
from services.payment import PaymentService
from models.order import Order
from patterns.observer.observers import EmailNotifier, LogNotifier


class CheckoutFacade:
    """
    Facade que simplifica todo o fluxo de compra:
    - recebe carrinho e informações de pagamento
    - calcula total
    - processa pagamento
    - cria pedido
    - registra observadores
    - atualiza status e dispara notificações
    """

    def __init__(self):
        self.payment_service = PaymentService()

    def checkout(self, cart: ShoppingCart, order_id: str):
        """
        Executa o processo completo de finalização de compra.
        """
        total = cart.calculate_total(cart.amount)

        # Processa pagamento
        if not self.payment_service.process_payment(total):
            print("[Checkout] Pagamento falhou!")
            return None

        # Cria pedido
        order = Order(order_id)

        # Registra observadores
        order.attach(EmailNotifier())
        order.attach(LogNotifier())

        # Atualiza status
        order.set_status("Pago")
        order.set_status("Enviado")
        order.set_status("Concluído")

        print(f"[Checkout] Pedido {order_id} finalizado com sucesso!")
        return order

