from typing import List
from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Interface base para todos os observadores.
    """

    @abstractmethod
    def update(self, message: str):
        pass


class Subject:
    """
    Classe base que gerencia uma lista de observadores.
    """

    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer):
        """
        Registra um observador.
        """
        self._observers.append(observer)

    def detach(self, observer: Observer):
        """
        Remove um observador registrado.
        """
        self._observers.remove(observer)

    def notify(self, message: str):
        """
        Notifica todos os observadores sobre uma mudança.
        """
        for observer in self._observers:
            observer.update(message)

