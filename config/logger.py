import datetime
import logging
from config.settings import LOG_DIR, DEBUG

_log_format = '%(asctime)s [LINE:%(lineno)d] %(levelname)s %(funcName)s %(module)s %(message)s'


def get_file_handler():
    file_handler = logging.FileHandler(f"{LOG_DIR}/bot{datetime.date.today().strftime('%d-%m-%Y')}.log")
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler


def get_stream_handler():
    stream_handler = logging.StreamHandler()
    if DEBUG:
        stream_handler.setLevel(logging.DEBUG)
    else:
        stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(_log_format))
    return stream_handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    return logger
