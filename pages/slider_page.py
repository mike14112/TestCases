from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage


class SliderPage(BasePage):
    LOC_UNIQUE_ELEM = "//*[@id='content']//h3"
    LOC_SLIDER = "//*[@type='range']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.unique_element = Label(driver=self.driver, locator=self.LOC_UNIQUE_ELEM,
                                    description='open url -> main_elem')
        self.slider_element = Button(driver=self.driver, locator=self.LOC_SLIDER,
                                     description='click input range to 5')

    def wait_unique(self):
        return self.unique_element.elem_visible().text.lower().strip()

    def move_to_slider(self):
        return self.slider_element.move_element()
