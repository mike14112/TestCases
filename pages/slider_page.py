import random

from elements.action_chains import Actions
from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage




class SliderPage(BasePage):
    LOC_UNIQUE_ELEM = "//*[@id='content']//h3"
    LOC_SLIDER = "//*[@type='range']"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.page_name = 'Slider Page'
        self.actions = Actions(self.browser)

        self.unique_elem = Label(driver=self.browser.driver, locator=self.LOC_UNIQUE_ELEM,
                                 description='open url -> unique element')
        self.slider_element = WebElement(driver=self.browser.driver, locator=self.LOC_SLIDER,
                                         description='select slider -> move slider')

    def move_to_slider(self, number, number2):
        random_number = random.randint(number, number2)
        for _ in range(random_number):
             self.actions.key_right(self.slider_element)
