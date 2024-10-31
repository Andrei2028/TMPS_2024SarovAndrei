from models.product import Product

class DiscountDecorator:
    def __init__(self, product):
        self.product = product

    def get_price(self):
        # Applies a 10% discount to the original price
        return self.product.get_price() * 0.9

class TaxDecorator:
    def __init__(self, product):
        self.product = product

    def get_price(self):
        # Applies a 5% tax to the price
        return self.product.get_price() * 1.05
