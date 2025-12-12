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
        self.page_name = 'Page  js Alert'

        self.unique_elem = Label(self.browser,
                                 locator=self.LOC_UNIQUE_ELEM, description="wait for open -> unique element")
        self.alert_btn_elem = Button(self.browser, locator=self.LOC_ALERT, description="btn alert -> alert")
        self.btn_confirm_elem = Button(self.browser, locator=self.LOC_CONFIRM,
                                       description="btn confirm -> confirm")

        self.alert_res = Label(self.browser, locator=self.LOC_RESULT, description="Alert confirm -> result")

    def click_btn_alert(self):
        self.alert_btn_elem.js_click()

    def click_btn_confirm(self):
        self.btn_confirm_elem.click()

    def get_res_text(self):
        return self.alert_res.get_text().lower().strip()
