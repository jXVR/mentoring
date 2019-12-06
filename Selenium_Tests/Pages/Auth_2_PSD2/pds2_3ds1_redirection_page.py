from selenium.webdriver.common.by import By
from Selenium_Tests.Lib.lib import Lib


class FallbackPage:

    def __init__(self, driver):
        self.driver = driver
        self.lib = Lib(driver)


    user_name_field_css = "#username"
    password_field_css = "#password"
    submit_button_css = ".button"

    def fill_username_field(self, text):
        username_field = self.driver.find_element_by_css_selector(self.user_name_field_css)
        username_field.clear()
        username_field.send_keys(text)

    def fill_password_field(self, text):
        password_field = self.driver.find_element_by_css_selector(self.password_field_css)
        password_field.clear()
        password_field.send_keys(text)

    def submit_button_click(self):
        submit_button = self.driver.find_element_by_css_selector(self.submit_button_css)
        submit_button.click()

    def wait_for_page_to_be_open(self):
        self.lib.wait_for_element(self.submit_button_css, By.CSS_SELECTOR)

    def complete_fallback_scenario(self, username, password):
        self.wait_for_page_to_be_open()
        self.fill_username_field(username)
        self.fill_password_field(password)
        self.submit_button_click()