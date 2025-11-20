from .subject import Observer


class EmailNotifier(Observer):
    """
    Observador que simula envio de e-mail para o cliente.
    """

    def update(self, message: str):
        print(f"[Email] Mensagem enviada ao cliente: {message}")


class LogNotifier(Observer):
    """
    Observador que registra eventos no sistema.
    """

    def update(self, message: str):
        print(f"[Log] Evento registrado: {message}")

