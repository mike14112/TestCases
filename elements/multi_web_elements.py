from elements.web_element import WebElement


class MultiWebElementsPage:
    def __init__(self, driver, formatable_xpath, description):
        self.index = 1
        self.driver = driver
        self.formatable_xpath = formatable_xpath
        self.description = description

    def __iter__(self):
        self.index = 1
        return self

    def __next__(self):
        current_elem = (
            WebElement(self.driver,
                       self.formatable_xpath.format(self.index),
                       f'{self.description}'))

        if not current_elem.is_exists():
            raise StopIteration
        else:
            self.index += 1
            return current_elem
