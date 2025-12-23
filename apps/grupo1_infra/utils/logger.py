
import logging
from logging.handlers import RotatingFileHandler

def setup_logger():
    logger = logging.getLogger("project")
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler("project.log", maxBytes=1000000, backupCount=3)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
