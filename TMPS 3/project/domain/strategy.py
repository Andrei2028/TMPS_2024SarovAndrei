# domain/strategy.py

from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass

class NoDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, price):
        return price * (1 - self.percentage / 100)

class FixedDiscount(DiscountStrategy):
    def __init__(self, amount):
        self.amount = amount

    def apply_discount(self, price):
        return max(price - self.amount, 0)  # Ensure price doesn't go below zero
