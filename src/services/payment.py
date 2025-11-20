class PaymentService:
    """
    Serviço que simula o processamento de pagamento.
    """

    def process_payment(self, amount: float) -> bool:
        """
        Simula validação de pagamento.
        Em um sistema real, haveria integração externa.
        """
        print(f"[Pagamento] Processando pagamento de R$ {amount:.2f}...")
        return True

