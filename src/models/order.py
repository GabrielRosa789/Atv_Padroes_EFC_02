from patterns.observer.subject import Subject


class Order(Subject):
    """
    Pedido que pode mudar de status.
    Ao mudar de status, notifica os observadores.
    """

    def __init__(self, order_id: str):
        super().__init__()
        self.order_id = order_id
        self.status = "Criado"

    def set_status(self, new_status: str):
        """
        Atualiza o status e notifica os observadores.
        """
        self.status = new_status
        self.notify(f"Pedido {self.order_id} agora está: {self.status}")

