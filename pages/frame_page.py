from elements.button import Button
from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class IFramePage(BasePage):
    LOC_UNIQUE_ELEM = "//*[@id='framesWrapper']//h1"
    LOC_BTN_ALERT_LIST = "//*[contains(@class, 'header-text') and contains (., 'Alerts, Frame & Windows')]"
    LOC_BTN_NESTED_FRAMES = "//span[contains(text(), 'Nested Frames')]"
    LOC_UNIQUE_ELEM_NESTED_FRAME = "//*[@id='framesWrapper']//h1"
    LOC_PARENT_FRAME_TEXT = "//body[contains(text(), 'Parent frame')]"
    LOC_CHILD_FRAME_TEXT = "//*[contains(text(), 'Child Iframe')]"
    LOC_FRAME_ELEM = "//span[contains(text(), 'Frames')]"
    LOC_FRAME_UNIQUE_PAGE = "//*[@id='framesWrapper']//h1"
    LOC_TEXT_FRAME = 'sampleHeading'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.unique_main_page_elem = Label(self.driver, self.LOC_UNIQUE_ELEM, description='open browser -> unique elem')
        self.btn_list_alerts = Button(self.driver, self.LOC_BTN_ALERT_LIST,
                                      description='click btn list frames -> show list alerts and frames')
        self.btn_nested_frames = Button(self.driver, self.LOC_BTN_NESTED_FRAMES,
                                        description='click btn frames -> show nested frames')
        self.unique_nested_frame_page = Label(self.driver, self.LOC_UNIQUE_ELEM_NESTED_FRAME,
                                              description='click btn nested frames -> show nested page '
                                                          'frames text text ')

        self.parent_frame_text = Label(self.driver, self.LOC_PARENT_FRAME_TEXT,
                                       description='switch from parent frame to text parent frame')
        self.child_frame_text = WebElement(self.driver, self.LOC_CHILD_FRAME_TEXT,
                                           description='switch to child frames -> child frame')
        self.frame_elem = Button(self.driver, self.LOC_FRAME_ELEM, description='click frame elem -> page open frame')
        self.unique_elem_frame_text = Label(self.driver, self.LOC_FRAME_UNIQUE_PAGE,
                                            description='click frame elem -> show unique elem page')
        self.frame_text = Label(self.driver, self.LOC_TEXT_FRAME, description=' open  page frame -> show frame text')

    def get_unique_elem(self):
        return self.unique_main_page_elem.get_text().lower().strip()

    def click_btn_list_alerts(self):
        return self.btn_list_alerts.btn_click()

    def click_nested_frames(self):
        return self.btn_nested_frames.btn_click()

    def get_unique_text_nested_frames(self):
        return self.unique_nested_frame_page.get_text().lower().strip()

    def get_text_parent_frame(self):
        return self.parent_frame_text.get_text().lower().strip()

    def get_text_child_frame(self):
        return self.child_frame_text.get_text().lower().strip()

    def click_frame_menu(self):
        return self.frame_elem.btn_click()

    def get_text_unique_frame_page(self):
        return self.unique_elem_frame_text.get_text().lower().strip()

    def get_text_frame(self):
        return self.frame_text.get_text().lower().strip()
