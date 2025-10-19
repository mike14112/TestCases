import time

from logger import logger
import pyautogui

class PyAutoGui:
    @staticmethod
    def upload_file(file_path):
        logger.Logger.info('show dialog window')
        time.sleep(3)
        logger.Logger.info(f'write {file_path} to search file dialog write')
        pyautogui.write(file_path)
        logger.Logger.info('Press enter')
        pyautogui.press('enter')
        time.sleep(3)
