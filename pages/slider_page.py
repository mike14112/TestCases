from selenium.webdriver.common.by import By

from element.button import Button
from element.label import Label
from pages.base_page import BasePage


class SliderPage(BasePage):
    LOQ_UNIQUE_ELEM = (By.XPATH, "//*[@id='content']//h3")
    LOQ_SLIDER = (By.XPATH, "//*[@type='range']")

    def __init__(self, driver):
        super().__init__(driver)
        self.unique_element = Label(driver=self.driver, locator=self.LOQ_UNIQUE_ELEM,
                                    description='open url -> main_elem')
        self.slider_element = Button(driver=self.driver, locator=self.LOQ_SLIDER, description='click input range to 5')

    def wait_element(self):
        return self.unique_element.elem_visible()

    def move_to_slider(self):
        return self.slider_element.move_element()
