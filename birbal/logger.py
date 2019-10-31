import logging
import  os

def setup_logger(logger_dir, level=logging.DEBUG, name='question_notification'):
    if not os.path.exists(logger_dir):
        os.makedirs(logger_dir)
    logger_path = os.path.join(logger_dir, 'question_notification.log')
    logger = logging.getLogger(name)
    logger.setLevel(level)

    terminal_handler = logging.StreamHandler()
    terminal_handler.setFormatter(logging.Formatter("[%(levelname)s] %(asctime)s : %(message)s"))
    terminal_handler.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(logger_path, mode='a')
    file_handler.setFormatter(logging.Formatter("[%(levelname)s] %(asctime)s %(filename)s:%(lineno)s : %(message)s"))
    file_handler.setLevel(logging.DEBUG)

    logger.addHandler(terminal_handler)
    logger.addHandler(file_handler)
    return logger
