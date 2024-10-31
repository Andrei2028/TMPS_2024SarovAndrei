# utilities/logger.py

import logging

def get_logger():
    logger = logging.getLogger("ProductSystem")
    logger.setLevel(logging.INFO)

    if not logger.hasHandlers():
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger
