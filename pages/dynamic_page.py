from elements.label import Label
from elements.multi_web_elements import MultiWebElements
from pages.base_page import BasePage


class DynamicPage(BasePage):
    LOC_UNIQUE_ELEM = "//*[contains(@class, 'example')]//h3"
    LOC_IMGS = "(//*[@id='content']//img)[{}]"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.page_name = 'Dynamic Page'

        self.unique_elem = Label(self.browser, self.LOC_UNIQUE_ELEM, 'open url -> unique element')
        self.imgs = MultiWebElements(self.browser, self.LOC_IMGS, 'page show -> show img  ')

    def get_all_src(self):
        return [img.get_attribute('src') for img in self.imgs]
