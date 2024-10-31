class LegacyProduct:
    def old_get_item(self):
        return "Legacy Product: ID = 1"

class ProductAdapter:
    def __init__(self, legacy_product):
        self.legacy_product = legacy_product

    def get_product(self):
        return self.legacy_product.old_get_item()
