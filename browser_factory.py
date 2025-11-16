from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BrowserFactory:
    @staticmethod
    def get_browser_instance():
        options = Options()
        return webdriver.Chrome(options=options)
