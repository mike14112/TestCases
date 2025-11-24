from bs4 import BeautifulSoup

from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class ScrollPage(BasePage):
    LOC_UNIQUE_ELEM = "//*[@id='content']//h3"
    LOC_SCROLL_ELEM = "//*[contains(@class, 'jscroll-inner')]"
    LOC_PARAGRAPH_ELEM = "//*[contains(@class, 'jscroll-added')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.page_name = 'scroll page'

        self.unique_elem = Label(self.browser,
                                 self.LOC_UNIQUE_ELEM, 'open page -> show unique element')
        self.btn_scroll = WebElement(self.browser,
                                     self.LOC_SCROLL_ELEM, 'open page -> show scroll element')
        self.paragraph_elem = WebElement(self.browser,
                                         self.LOC_PARAGRAPH_ELEM, 'scroll page -> show paragraph element')

    def key_down(self):
        self.actions.key_down(self.btn_scroll)

    def scroll_to_end(self):
        self.btn_scroll.scroll_to()

    def get_paragraph(self, number):
        result = []
        while len(result) < number:
            html = self.paragraph_elem.get_attribute('innerHtml')
            if not html:
                self.key_down()
                continue
            soup = BeautifulSoup(html, 'html.parser')
            rows = soup.find_all('br')

            for row in rows:
                result.append(row)
                if len(result) >= number:
                    break
            self.scroll_in_end()

        return result
