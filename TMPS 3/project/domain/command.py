# domain/command.py

class Command:
    def execute(self):
        pass

class ChangePriceCommand(Command):
    def __init__(self, product, new_price):
        self.product = product
        self.new_price = new_price

    def execute(self):
        print(f"Changing price of {self.product.name} to ${self.new_price:.2f}")
        self.product.set_price(self.new_price)
