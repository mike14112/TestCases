from elements.action_chains import Actions
from elements.button import Button
from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class HoversPage(BasePage):
    LOC_UNIQUE_ELEM = "//*[@id='content']//h3"
    LOC_USER_ELEM = "//*[contains(@class, 'figure')][{}]"
    LOC_USER_TEXT = "(//*[contains(@class, 'figcaption')])[{}]//h5"
    LOC_LINK_USER = "(//*[contains(text(), 'View profile')])[{}]"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.page_name = 'hovers page'
        self.actions = Actions(self.browser)

        self.unique_elem = Label(self.browser, self.LOC_UNIQUE_ELEM, description='open url -> unique element')


    def hover_user(self, index):
        loq_user = self.LOC_USER_ELEM.format(index)
        elem = WebElement(self.browser, loq_user, description='mouse to ->  user')
        self.actions.move_to_element(elem.wait_for_visibility())

    def get_user_info(self, index):
        loq_user_text = self.LOC_USER_TEXT.format(index)
        hover_user = Label(self.browser, loq_user_text, description='user -> user hover text')
        return hover_user.get_text().lower().strip()

    def open_user_link(self, index):
        loq_user_link = self.LOC_LINK_USER.format(index)
        link_user = Button(self.browser, loq_user_link, description=f'user -> user index: {index} ')
        return link_user.click()
