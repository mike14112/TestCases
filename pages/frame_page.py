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
    LOC_PARENT_FRAME = 'frame1'
    LOC_CHILD_FRAME = '//iframe[contains(@srcdoc, "Child Iframe")]'

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.page_name = 'IFrame Page'

        self.unique_elem = Label(self.browser, self.LOC_UNIQUE_ELEM,
                                 description='wait for open -> unique elem')
        self.btn_list_alerts = Button(self.browser, self.LOC_BTN_ALERT_LIST,
                                      description='click btn list frames -> show list alerts and frames')
        self.btn_nested_frames = Button(self.browser, self.LOC_BTN_NESTED_FRAMES,
                                        description='click btn frames -> show nested frames')
        self.unique_nested_frame_page = Label(self.browser, self.LOC_UNIQUE_ELEM_NESTED_FRAME,
                                              description='click btn nested frames -> show nested page '
                                                          'frames text text ')

        self.parent_frame_text = Label(self.browser, self.LOC_PARENT_FRAME_TEXT,
                                       description='switch from parent frame to text parent frame')
        self.child_frame_text = WebElement(self.browser, self.LOC_CHILD_FRAME_TEXT,
                                           description='switch to child frames -> child frame')
        self.frame_elem = Button(self.browser, self.LOC_FRAME_ELEM,
                                 description='click frame elem -> page open frame')
        self.unique_elem_frame_text = Label(self.browser, self.LOC_FRAME_UNIQUE_PAGE,
                                            description='click frame elem -> show unique elem page')
        self.frame_text = Label(self.browser, self.LOC_TEXT_FRAME,
                                description=' open  page frame -> show frame text')

        self.parent_frame = WebElement(self.browser, self.LOC_PARENT_FRAME,
                                       description='wait for open  -> show  frames elements')

        self.child_frame = WebElement(self.browser, self.LOC_CHILD_FRAME, 'parent frame -> child frame')

    def click_btn_list_alerts(self):
        self.btn_list_alerts.click()

    def click_nested_frames(self):
        self.btn_nested_frames.click()

    def get_unique_text_nested_frames(self):
        return self.unique_nested_frame_page.get_text().lower().strip()

    def get_text_parent_frame(self):
        return self.parent_frame_text.get_text().lower().strip()

    def get_text_child_frame(self):
        return self.child_frame_text.get_text().lower().strip()

    def click_frame_menu(self):
        self.frame_elem.click()

    def get_text_unique_frame_page(self):
        return self.unique_elem_frame_text.get_text().lower().strip()

    def get_text_frame(self):
        return self.frame_text.get_text().lower().strip()

    def switch_parent_frame(self):
        self.browser.switch_frame(self.parent_frame)

    def switch_child_frame(self):
        self.browser.switch_frame(self.child_frame)
