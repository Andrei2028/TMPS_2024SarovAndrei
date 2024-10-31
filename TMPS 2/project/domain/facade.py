from domain.adapter import ProductAdapter, LegacyProduct
from domain.decorator import DiscountDecorator, TaxDecorator
from models.product import Product

class ProductFacade:
    def __init__(self):
        self.legacy_product = ProductAdapter(LegacyProduct())
        self.product = Product("New Product", 100)

    def get_legacy_product(self):
        # Uses the adapter to access legacy functionality
        return self.legacy_product.get_product()

    def get_discounted_price(self):
        # Applies the discount decorator
        discounted_product = DiscountDecorator(self.product)
        return discounted_product.get_price()

    def get_final_price(self):
        # Applies both discount and tax decorators
        final_product = TaxDecorator(DiscountDecorator(self.product))
        return final_product.get_price()
