from domain.facade import ProductFacade
from utilities.logger import get_logger

def main():
    logger = get_logger()
    product_facade = ProductFacade()

    logger.info("Legacy product through adapter: %s", product_facade.get_legacy_product())
    logger.info("Discounted price: %s", product_facade.get_discounted_price())
    logger.info("Final price with tax: %s", product_facade.get_final_price())

if __name__ == "__main__":
    main()
