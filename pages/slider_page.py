from elements.action_chains_element import ActionChainsElement

from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage


class SliderPage(BasePage):
    LOQ_UNIQUE_ELEM = "//*[@id='content']//h3"
    LOQ_SLIDER = "//*[@type='range']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.unique_element = Label(driver=self.driver, locator=self.LOQ_UNIQUE_ELEM,
                                    description='open url -> main_elem')
        self.slider_element = Button(driver=self.driver, locator=self.LOQ_SLIDER,
                                                  description='click input range to 5')

    def wait_element(self):
        return self.unique_element.elem_visible()

    def move_to_slider(self):
        return self.slider_element.move_to_slider()
