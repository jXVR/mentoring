from selenium.webdriver.common.by import By
from Selenium_Tests.Lib.lib import Lib


class ConfirmationPageMassive:

    def __init__(self, driver):
        self.driver = driver
        self.lib = Lib(driver)

    confirmation_page_css = ".ConfirmationView"
    confirmation_button_css =".buttonText"

    def confirmation_button_click(self):
        confirmation_button_click = self.driver.find_element_by_css_selector(self.confirmation_button_css)
        confirmation_button_click.click()

    def wait_for_page_to_be_open(self):
        self.lib.wait_for_element(self.confirmation_page_css, By.CSS_SELECTOR)