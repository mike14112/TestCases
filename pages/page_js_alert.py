from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage


class PageJsAlert(BasePage):
    LOC_UNIQUE_ELEM = "//*[@class='example']//h3"
    LOC_ALERT = "//*[contains(@onclick, 'jsAlert()')]"
    LOC_CONFIRM = "//*[contains(@onclick, 'jsConfirm()')]"
    LOC_PROMPT = "//*[contains(@onclick, 'jsPrompt()')]"
    LOC_RESULT = "result"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.page_name ='Page  js Alert'

        self.unique_elem = Label(driver=self.browser.driver,
                                 locator=self.LOC_UNIQUE_ELEM, description="unique elem")
        self.alert_btn_elem = Button(driver=self.browser.driver, locator=self.LOC_ALERT, description="btn -> alert")
        self.btn_confirm_elem = Button(driver=self.browser.driver, locator=self.LOC_CONFIRM,
                                       description="btn -> confirm")

        self.alert_res = Label(driver=self.browser.driver, locator=self.LOC_RESULT, description="Alert -> result")

    def wait_unique(self):
        return self.unique_elem.is_displayed().text.lower()

    def click_btn_alert(self):
        return self.alert_btn_elem.js_click()

    def result_wait(self):
        return self.alert_res.elem_fast_wait().text.lower().strip()

    def btn_confirm(self):
        return self.btn_confirm_elem.btn_click()
