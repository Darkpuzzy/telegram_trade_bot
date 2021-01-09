import logging


def create_logger() -> logging.Logger:
    _logger = logging.getLogger(__name__)

    stream_handler = logging.StreamHandler()
    stream_formatter = logging.Formatter(''.join([
        '[%(asctime)-15s]',
        '[%(name)s] - ',
        '[ %(levelname)s ] -',
        ' %(message)s',
    ]))
    stream_handler.setFormatter(stream_formatter)

    stream_handler.setLevel(logging.DEBUG)

    _logger.addHandler(stream_handler)
    _logger.setLevel(logging.DEBUG)

    return _logger


logger: logging.Logger = create_logger()
