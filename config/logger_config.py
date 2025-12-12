import logging

import os


class LoggerConfig:
    LOGS_DIR_NAME = 'logs'
    LOGGER_NAME = 'logger'
    LOGGER_FILE_NAME = LOGS_DIR_NAME + os.sep + 'logger.log'
    LOGS_LEVEL = logging.INFO
    MAX_BYTES = 100000
    BACKUP_COUNT = 10
    LOGGER_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    DATE_FORMAT = '%d/%m/%Y %H:%M:%S'
