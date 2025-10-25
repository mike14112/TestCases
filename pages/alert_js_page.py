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

        self.unique_elem = Label(driver=self.browser.driver,
                                 locator=self.LOC_UNIQUE_ELEM, description="unique elem")
        self.alert_btn_elem = Button(driver=self.browser.driver, locator=self.LOC_ALERT, description="btn -> alert")
        self.btn_confirm_elem = Button(driver=self.browser.driver, locator=self.LOC_CONFIRM, description="btn -> confirm")
        self.alert_res = Label(driver=self.browser.driver, locator=self.LOC_RESULT, description="Alert -> result")

    def get_unique_elem(self):
        return self.unique_elem.elem_visible()

    def click_btn_alert(self):
        return self.alert_btn_elem.js_click()

    def result_wait(self):
        return self.alert_res.elem_fast_wait()

    def btn_confirm(self):
        return self.btn_confirm_elem.js_click()
