from elements.button import Button
from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class ScrollPage(BasePage):
    LOQ_UNIQUE_ELEM = "//*[@id='content']//h3"
    LOQ_SCROLL_ELEM = "//*[contains(@class, 'jscroll-inner')]"
    LOQ_PARAGRAPH_ELEMS = "//*[contains(@class, 'jscroll-added')]"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.unique_elems = Label(self.driver, self.LOQ_UNIQUE_ELEM, 'open page -> show unique element')
        self.btn_scroll = Button(self.driver, self.LOQ_SCROLL_ELEM, 'open page -> show scroll element')
        self.paragraph_elems = WebElement(self.driver,
                                          self.LOQ_PARAGRAPH_ELEMS, 'open page -> show paragraph element')

    def get_unique_elem(self):
        return self.unique_elems.elem_visible()

    def key_down(self):
        return self.btn_scroll.key_down()

    def count_paragraph(self):
        while len(self.paragraph_elems.wait_for_all_elems()) < 30:
            self.btn_scroll.key_down()
        else:
            return True


