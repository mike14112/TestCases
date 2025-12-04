import random

from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class SliderPage(BasePage):
    LOC_UNIQUE_ELEM = "//*[@id='content']//h3"
    LOC_SLIDER = "//*[@type='range']"
    LOC_SLIDER_RES = 'range'

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.page_name = 'Slider Page'

        self.unique_elem = Label(self.browser, locator=self.LOC_UNIQUE_ELEM,
                                 description='open url -> unique element')
        self.slider_element = WebElement(self.browser, locator=self.LOC_SLIDER,
                                         description='select slider -> move slider')
        self.slider_res = Label(self.browser, locator=self.LOC_SLIDER_RES, description='slider res')

    def move_to_slider(self, number, number2):
        target_value = random.randint(number, number2)

        for _ in range(target_value):
            current = int(self.slider_res.get_text())
            self.actions.key_right(self.slider_element)
            if current == 0:
                self.actions.key_left(self.slider_element)

    def get_min_step(self):
        min_step = self.slider_element.get_property("min")
        return round(float(min_step))

    def get_max_step(self):
        max_step = self.slider_element.get_property('max')
        return round(float(max_step))
