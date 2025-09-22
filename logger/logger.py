import logging.handlers
import os
import sys

from config.logger_config import LoggerConfig


class Logger:
    if not os.path.isdir(LoggerConfig.LOGS_DIR_NAME):
        os.makedirs(LoggerConfig.LOGS_DIR_NAME)
    __logger = logging.getLogger(LoggerConfig.LOGGER_NAME)
    __logger.setLevel(LoggerConfig.LOGS_LEVEL)
    __handler1 = logging.handlers.RotatingFileHandler(LoggerConfig.LOGGER_FILE_NAME, maxBytes=LoggerConfig.MAX_BYTES,
                                                      backupCount=LoggerConfig.BACKUP_COUNT)

    __handler2 = logging.StreamHandler(sys.stdout)
    __formatter = logging.Formatter(LoggerConfig.LOGGER_FORMAT)
    __handler1.setFormatter(__formatter)
    __handler2.setFormatter(__formatter)
    __logger.addHandler(__handler1)
    __logger.addHandler(__handler2)

    @staticmethod
    def set_level(level) -> None:
        Logger.__logger.setLevel(level)

    @staticmethod
    def info(message) -> None:
        Logger.__logger.info(message)

    @staticmethod
    def debug(message) -> None:
        Logger.__logger.debug(message)

    @staticmethod
    def warning(message) -> None:
        Logger.__logger.warning(message)

    @staticmethod
    def error(message) -> None:
        Logger.__logger.error(message)

    @staticmethod
    def critical(message) -> None:
        Logger.__logger.critical(message)
