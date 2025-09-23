from selenium.webdriver.common.by import By

from element.base_element import BaseElement
from pages.base_page import BasePage


class PageAlert(BasePage):
    LOQ_UNIQUE_ELEM = (By.XPATH, "//*[contains(text(), 'Here are some examples of different "
                                 "JavaScript alerts which can be troublesome for automation')]")
    LOQ_ALERT = (By.XPATH, "//*[contains(@onclick, 'jsAlert()')]")
    LOQ_CONFIRM = (By.XPATH, "//*[contains(@onclick, 'jsConfirm()')]")
    LOQ_PROMPT = (By.XPATH, "//*[contains(@onclick, 'jsPrompt()')]")
    LOQ_RESULT = (By.ID, "result")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.unique_elem = BaseElement(driver=self.driver,
                                       locator=self.LOQ_UNIQUE_ELEM, description="unique elem")
        self.alert_btn_elem = BaseElement(driver=self.driver, locator=self.LOQ_ALERT, description="btn -> alert")
        self.btn_confirm_elem = BaseElement(driver=self.driver, locator=self.LOQ_CONFIRM, description="btn -> confirm")
        self.alert_res = BaseElement(driver=self.driver, locator=self.LOQ_RESULT, description="Alert -> result")

    def wait_unique(self):
        return self.unique_elem.elem_text()

    def click_btn_alert(self):
        return self.alert_btn_elem.btn_click()

    def result_wait(self):
        return self.alert_res.elem_fast_wait()

    def btn_confirm(self):
        return self.btn_confirm_elem.btn_click()
