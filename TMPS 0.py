class Logger:
    def log(self, message):
        print(message)


class FileLogger(Logger):
    def log(self, message):
        with open("log.txt", "a") as file:
            file.write(message + "\n")


class Order:
    def __init__(self, items, logger: Logger):
        self.items = items
        self.logger = logger

    def add_item(self, item):
        self.items.append(item)
        self.logger.log(f"Item added: {item}")

    def remove_item(self, item):
        self.items.remove(item)
        self.logger.log(f"Item removed: {item}")


class OrderCalculator:
    def calculate_total(self, order):
        return sum(order.items)


logger = FileLogger()
order = Order([10, 20, 30], logger)
order.add_item(40)
order.remove_item(20)
calculator = OrderCalculator()
total = calculator.calculate_total(order)
logger.log(f"Total order price: {total}")
