from bs4 import BeautifulSoup

from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class ScrollPage(BasePage):
    LOC_UNIQUE_ELEM = "//*[@id='content']//h3"
    LOC_ALL_PARAGRAPH = "//div[contains(@class, 'jscroll-inner')]"
    LOC_PARAGRAPH_ELEM = "//div[contains(@class, 'jscroll-added')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.page_name = 'scroll page'

        self.unique_elem = Label(self.browser,
                                 self.LOC_UNIQUE_ELEM, 'wait for open -> show unique element')
        self.all_paragraph_elem = WebElement(self.browser,
                                             self.LOC_ALL_PARAGRAPH,
                                             'div paragraph elem -> show main  div elements')
        self.paragraph_elem = WebElement(self.browser,
                                         self.LOC_PARAGRAPH_ELEM, 'scroll page -> show paragraph element')

    def get_paragraph(self, number):
        while True:
            self.all_paragraph_elem.scroll_to()
            soup = BeautifulSoup(self.all_paragraph_elem.get_attribute('innerHTML'), 'html.parser')
            rows = soup.find_all(class_='jscroll-added')
            if len(rows) == number:
                return rows
