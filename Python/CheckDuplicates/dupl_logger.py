from asyncio.log import logger


def log_info(msg: str):
    logger.info(msg)


def log_error(msg: str):
    logger.error(msg)
