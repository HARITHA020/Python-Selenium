import logging
def log_generator():
    logger = logging.getLogger("automationLogger")

    if not logger.handlers:
        logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler("testlogreport.log")
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger