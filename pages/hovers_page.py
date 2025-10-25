from elements.button import Button
from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class HoversPage(BasePage):
    LOC_UNIQUE_ELEM = "//*[@id='content']//h3"
    LOC_USER_ELEM = "//*[contains(@class, 'figure')][{}]"
    LOC_USER_TEXT = "(//*[contains(@class, 'figcaption')])[{}]//h5"
    LOC_LINK_USER = "(//*[contains(text(), 'View profile')])[{}]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.unique_elem = Label(self.driver, self.LOC_UNIQUE_ELEM, description='open url -> main page')

    def wait_unique(self):
        return self.unique_elem.elem_visible().text.lower().strip(' ')

    def hover_user(self, index):
        loq_user = self.LOC_USER_ELEM.format(index)
        elem = WebElement(self.driver, loq_user, description='mouse to ->  user')
        return elem.move_element()

    def get_user_info(self, index):
        loq_user_text = self.LOC_USER_TEXT.format(index)
        hover_user = Label(self.driver, loq_user_text, description='user -> user hover text')
        return hover_user.get_text().lower().strip('')

    def open_user_link(self, index):
        loq_user_link = self.LOC_LINK_USER.format(index)
        link_user = Button(self.driver, loq_user_link, description='user -> user link')
        return link_user.btn_click()
