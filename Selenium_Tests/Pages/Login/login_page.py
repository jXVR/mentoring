from selenium.webdriver.common.by import By
from Selenium_Tests.Lib.lib import Lib


class LoginPage:
    url = 'https://stag.dazn.com/en-DE/account/signin'

    def __init__(self, driver):
        self.driver = driver
        self.lib = Lib(driver)

    # selectors
    cookie_button_css = "[data-test-id=\"cookie-disclaimer-button\"]"

    email_field_css_selector = '#email--1'
    email_field_empty_error_css = "[data-test-id=\"error-message-EMAIL-is-not-empty\"]"
    email_field_valid_error_css = "[data-test-id=\"error-message-EMAIL-is-email\"]"

    password_field_css_selector = '#password--2'
    password_field_old_length_error_css = "[data-test-id=\"error-message-PASSWORD-invalid-old-password-lenght\"]"


    login_button_css_selector = "[data-test-id=\"signIn__BUTTON\"]"
    # jesli dane sa niepoprawne button jest dissabled - disabled="", jesli sa poprawne, ta klasa znika

    show_password_css = "[data-test-id=\"SHOW_PASSWORD\"]"
    # jak zwalidowac czy password jest ukryty / zakryty - value jest caly czas takie samo

    forgot_email_link_css = "div.markdown___content___2AOZ5:nth-child(1) > p:nth-child(1) > a:nth-child(1)"
    forgot_password_link_css = "div.markdown___content___2AOZ5:nth-child(1) > p:nth-child(1) > a:nth-child(2)"
    sign_up_link_css = "div.markdown___content___2AOZ5:nth-child(2) > p:nth-child(1) > a:nth-child(1)"

    language_switcher_en_css = "[data-test-id=\"language-switcher-en\"]"


    #actions

    def cookie_button_click(self):
        self.driver.find_element_by_css_selector(self.cookie_button_css).click()

    def fill_email_field(self, text):
        email_field = self.driver.find_element_by_css_selector(self.email_field_css_selector)
        email_field.clear()
        email_field.send_keys(text)

    def fill_password_field(self, text):
        password_field = self.driver.find_element_by_css_selector(self.password_field_css_selector)
        password_field.clear()
        password_field.send_keys(text)

    def click_login_button(self):
        self.driver.find_element_by_css_selector(self.login_button_css_selector).click()

    def password_link_click(self):
        self.driver.find_element_by_css_selector(self.forgot_email_link_css).click()

    def forgot_email_link_click(self):
        self.driver.find_element_by_css_selector(self.forgot_password_link_css).click()

    def sign_up_lick_click(self):
        self.driver.find_element_by_css_selector(self.sign_up_link_css).click()

    def language_switcher_en_click(self):
        self.driver.find_element_by_css_selector(self.language_switcher_en_css).click()

    def language_switcher_regional_click(self, region):
        language_switcher_regional_css = f"[data-test-id=\"language-switcher-{region}\"]"
        switch = self.driver.find_element_by_css_selector(language_switcher_regional_css)
        switch.click()

    # def language_switcher_region(self, region):
    #     language_switcher_regional_css = f"[data-test-id=\"language-switcher-{region}\"]"
    #     return language_switcher_regional_css
    #
    # def language_switcher_regional_click(self):
    #     switch = self.driver.find_element_by_css_selector(self.language_switcher_regional_css)
    #     switch.click()

    def wait_for_page_to_be_open(self):
        self.lib.wait_for_element(self.email_field_css_selector, By.CSS_SELECTOR)

    #functions

    def login(self, email, password):
        self.wait_for_page_to_be_open()
        self.cookie_button_click()
        self.fill_email_field(email)
        self.fill_password_field(password)
        self.click_login_button()

    def switch_region(self, region_code):
        self.wait_for_page_to_be_open()
        self.cookie_button_click()
        # self.language_switcher_region(region_code)
        self.language_switcher_regional_click(region_code)