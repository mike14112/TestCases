from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage


class AlertJsPage(BasePage):
    LOQ_UNIQUE_ELEM = "//*[contains(text(), 'Here are some examples of different " \
                      "JavaScript alerts which can be troublesome for automation')]"
    LOQ_ALERT = "//*[contains(@onclick, 'jsAlert()')]"
    LOQ_CONFIRM = "//*[contains(@onclick, 'jsConfirm()')]"
    LOQ_PROMPT = "//*[contains(@onclick, 'jsPrompt()')]"
    LOQ_RESULT = "result"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.unique_elem = Label(driver=self.driver,
                                 locator=self.LOQ_UNIQUE_ELEM, description="unique elem")
        self.alert_btn_elem = Button(driver=self.driver, locator=self.LOQ_ALERT, description="btn -> alert")
        self.btn_confirm_elem = Button(driver=self.driver, locator=self.LOQ_CONFIRM, description="btn -> confirm")
        self.alert_res = Label(driver=self.driver, locator=self.LOQ_RESULT, description="Alert -> result")

    def wait_unique(self):
        return self.unique_elem.elem_visible()

    def click_btn_alert(self):
        return self.alert_btn_elem.js_click()

    def result_wait(self):
        return self.alert_res.elem_fast_wait()

    def btn_confirm(self):
        return self.btn_confirm_elem.js_click()
