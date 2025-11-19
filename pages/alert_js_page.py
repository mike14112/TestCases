from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage


class AlertJsPage(BasePage):
    LOC_UNIQUE_ELEM = "//*[contains(text(), 'Here are some examples of different " \
                      "JavaScript alerts which can be troublesome for automation')]"
    LOC_ALERT = "//*[contains(@onclick, 'jsAlert()')]"
    LOC_CONFIRM = "//*[contains(@onclick, 'jsConfirm()')]"
    LOC_PROMPT = "//*[contains(@onclick, 'jsPrompt()')]"
    LOC_RESULT = "result"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.page_name = 'alert js page'

        self.unique_elem = Label(self.browser,
                                 locator=self.LOC_UNIQUE_ELEM, description="unique elem")
        self.alert_btn_elem = Button(self.browser, locator=self.LOC_ALERT, description="btn alert  -> call alert")
        self.btn_confirm_elem = Button(self.browser, locator=self.LOC_CONFIRM,
                                       description="btn confirm -> call confirm")
        self.alert_res_elem = Label(self.browser, locator=self.LOC_RESULT, description="Alert confirm  -> result")

    def click_btn_alert(self):
        self.alert_btn_elem.js_click()

    def get_result_text(self):
        return self.alert_res_elem.get_text()

    def confirm_btn(self):
        self.btn_confirm_elem.js_click()
