from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage


class PageAlert(BasePage):
    LOQ_UNIQUE_ELEM = '//*[@class="example"]//h3'
    LOQ_ALERT = "//*[contains(@onclick, 'jsAlert()')]"
    LOQ_CONFIRM = "//*[contains(@onclick, 'jsConfirm()')]"
    LOQ_PROMPT = "//*[contains(@onclick, 'jsPrompt()')]"
    LOQ_RESULT = "result"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.unique_elem = Label(driver=self.driver,
                                 locator=self.LOQ_UNIQUE_ELEM, description="open url -> mainPage")
        self.alert_btn_elem = Button(driver=self.driver, locator=self.LOQ_ALERT, description="btn -> alert")
        self.btn_confirm_elem = Button(driver=self.driver, locator=self.LOQ_CONFIRM, description="btn -> confirm")
        self.alert_res = Label(driver=self.driver, locator=self.LOQ_RESULT, description="Alert -> result")

    def wait_unique(self):
        return self.unique_elem.elem_visible().text.lower().strip(' ')

    def click_btn_alert(self):
        return self.alert_btn_elem.btn_click()

    def result_wait(self):
        return self.alert_res.elem_fast_wait().text.lower().strip(' ')

    def btn_confirm(self):
        return self.btn_confirm_elem.btn_click()
