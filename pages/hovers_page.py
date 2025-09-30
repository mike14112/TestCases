from elements.button import Button
from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class HoversPage(BasePage):
    LOQ_UNIQUE_ELEM = "//*[@id='content']//h3"
    LOQ_USER_ELEM = "//*[contains(@class, 'figure')][{}]"
    LOQ_USER_TEXT = "(//*[contains(@class, 'figcaption')])[{}]//h5"
    LOQ_LINK_USER = "(//*[contains(text(), 'View profile')])[{}]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.unique_elem = Label(self.driver, self.LOQ_UNIQUE_ELEM, description='open url -> main page')

    def wait_elem(self):
        return self.unique_elem.get_text()

    def hover_user(self, index):
        loq_user = self.LOQ_USER_ELEM.format(index)
        elem = WebElement(self.driver, loq_user, description='mouse to ->  user')
        return elem.move_to_element()

    def get_user_info(self, index):
        loq_user_text = self.LOQ_USER_TEXT.format(index)
        hover_user = Label(self.driver, loq_user_text, description='user -> user hover text')
        return hover_user.get_text()

    def open_user_link(self, index):
        loq_user_link = self.LOQ_LINK_USER.format(index)
        link_user = Button(self.driver, loq_user_link, description='user -> user link')
        return link_user.elem_click()
