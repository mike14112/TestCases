from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class DynamicPage(BasePage):
    LOC_UNIQUE_ELEM = "//*[contains(@class, 'example')]//h3"
    LOC_IMG_1 = "(//*[@id='content']//img)[1]"
    LOC_IMG_2 = "(//*[@id='content']//img)[1]"
    LOC_IMG_3 = "(//*[@id='content']//img)[1]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.unique_elem = Label(self.driver.driver, self.LOC_UNIQUE_ELEM, 'open url -> show page')
        self.img1 = WebElement(self.driver.driver, self.LOC_IMG_1, 'page show -> show img 1')
        self.img2 = WebElement(self.driver.driver, self.LOC_IMG_2, 'page show -> show img 2')
        self.img3 = WebElement(self.driver.driver, self.LOC_IMG_3, 'page show -> show img 3')

    def get_unique_element(self):
        return self.unique_elem.elem_visible()

    def get_img1(self):
        return self.img1.get_attribute('src')

    def get_img2(self):
        return self.img2.get_attribute('src')

    def get_img3(self):
        return self.img3.get_attribute('src')

    def match_img(self):
        while self.get_img1() != self.get_img2() or self.get_img2() != self.get_img3() or self.get_img3() != self.get_img1():
           return self.driver.refresh()
        else:
           return True

