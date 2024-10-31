# client/main.py

from domain.observer import Product, PriceObserver
from domain.command import ChangePriceCommand
from domain.strategy import PercentageDiscount
from utilities.logger import get_logger

def main():
    logger = get_logger()

    # Create product and observer instances
    product = Product("Laptop", 999.99)
    price_observer = PriceObserver()

    # Attach observer to product
    product.add_observer(price_observer)
    logger.info("PriceObserver added to the product.")

    # Create and execute commands to change price
    change_price_command = ChangePriceCommand(product, 899.99)
    change_price_command.execute()  # Notify observer

    # Apply discount strategy
    discount_strategy = PercentageDiscount(10)  # 10% discount
    discounted_price = discount_strategy.apply_discount(product.price)
    product.set_price(discounted_price)  # Notify observer again

if __name__ == "__main__":
    main()
