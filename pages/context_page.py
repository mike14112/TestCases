from elements.button import Button
from elements.label import Label


class ContextPage:
    LOQ_UNIQUE_ELEM = "//*[@id='content']//h3"
    lOQ_AREA_ELEM = "hot-spot"

    def __init__(self, driver):
        self.driver = driver

        self.unique_elem = Label(driver=self.driver, locator=self.LOQ_UNIQUE_ELEM, description='open page -> opening')
        self.area = Button(driver=self.driver, locator=self.lOQ_AREA_ELEM, description='button -> alert')

    def wait_elem(self):
        return self.unique_elem.elem_visible()

    def context_click(self):
        return self.area.context_click()
