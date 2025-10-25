from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage


class ContextPage(BasePage):
    LOC_UNIQUE_ELEM = "//*[@id='content']//h3"
    lOC_AREA_ELEM = "hot-spot"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.unique_elem = Label(driver=self.driver, locator=self.LOC_UNIQUE_ELEM, description='open page -> opening')
        self.area = Button(driver=self.driver, locator=self.lOC_AREA_ELEM, description='button -> alert')

    def wait_unique(self):
        return self.unique_elem.elem_visible().text.lower().strip(' ')

    def context_click(self):
        return self.area.context_click()
