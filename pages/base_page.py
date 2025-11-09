from logger.logger import Logger


class BasePage:

    def __init__(self, browser):
        LOC_UNIQUE_ELEM = None
        self.browser = browser
        self.page_name = None
        self.unique_elem = LOC_UNIQUE_ELEM

    def get_wait_unique(self):
        Logger.info(f'{self.page_name} waiting for open')
        return self.unique_elem.presence_of_element()
