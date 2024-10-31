# domain/observer.py

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, product_name, new_price):
        pass

class PriceObserver(Observer):
    def update(self, product_name, new_price):
        print(f"PriceObserver: {product_name} price updated to ${new_price:.2f}")

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self._observers = []

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def set_price(self, new_price):
        self.price = new_price
        self._notify_observers()

    def _notify_observers(self):
        for observer in self._observers:
            observer.update(self.name, self.price)
