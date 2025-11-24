from elements.action_chains import Actions
from logger.logger import Logger


class BasePage:
    LOC_UNIQUE_ELEM = None

    def __init__(self, browser):
        self.browser = browser
        self.page_name = None
        self.unique_elem = None
        self.actions = Actions(self.browser)

    def wait_for_open(self):
        Logger.info(f'{self.page_name} waiting for open')
        return self.unique_elem.wait_presence()
