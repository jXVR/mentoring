from Selenium_Tests.Lib.lib import Lib
from selenium.webdriver.common.by import By

class MenuDropdown:
    def __init__(self, driver):
        self.driver = driver
        self.lib = Lib(driver)

    menu_container_css = "[data-test-id=\"MY-DAZN-MENU-DROPDOWN\"]"
    settings_css = "[title=\"Settings\"]"
    my_account_css = ".header-nav___dropdown-right___2O8UQ > li:nth-child(2) > a:nth-child(1)"
    help_css = "[title=\"Help\"]"
    sign_out_css = "button.header-nav___dropdown-link___36opA"
    about_css = "[title=\"About\"]"
    privacy_policy_css = "[title=\"Privacy Policy and Cookie Notice\"]"
    terms_and_condition_css = "[title=\"Terms and Conditions\"]"
    app_version_css = "[data-test-id=\"APP_VERSION\"]"

    sign_out_banner_css = "[data-test-id=\"DIALOG_MODAL_CONTAINER\"]"
    sign_out_confirmation_button_css = "[aria-label=\"SIGN OUT\"]"
    sign_out_cancel_button_css = "[aria-label=\"CANCEL\"]"

    dazn_logo_help_page_css = ".logo"

    def click_settings_button(self):
        settings = self.driver.find_element_by_css_selector(self.settings_css)
        settings.click()

    def click_my_account_button(self):
        my_account = self.driver.find_element_by_css_selector(self.my_account_css)
        my_account.click()

    def click_help_button(self):
        help_button = self.driver.find_element_by_css_selector(self.help_css)
        help_button.click()

    def click_sign_out_button(self):
        sign_out = self.driver.find_element_by_css_selector(self.sign_out_css)
        sign_out.click()

    def about_button(self):
        about = self.driver.find_element_by_css_selector(self.about_css)
        about.click()

    def click_privacy_policy_button(self):
        privacy_policy = self.driver.find_element_by_css_selector(self.privacy_policy_css)
        privacy_policy.click()

    def click_terms_and_conditions_button(self):
        terms_and_conditions = self.driver.find_element_by_css_selector(self.terms_and_condition_css)
        terms_and_conditions.click()

    def click_sign_out_confirmation(self):
        sign_out_confirmation = self.driver.find_element_by_css_selector(self.sign_out_confirmation_button_css)
        sign_out_confirmation.click()

    def click_sign_out_cancelation(self):
        sign_out_cancelation = self.driver.find_element_by_css_selector(self.sign_out_cancel_button_css)
        sign_out_cancelation.click()

    def click_dazn_logo_on_help_page(self):
        logo_on_help_page = self.driver.find_element_by_css_selector(self.dazn_logo_help_page_css)
        logo_on_help_page.click()

    def wait_for_menu_drop_down(self):
        self.lib.wait_for_element(self.menu_container_css, By.CSS_SELECTOR)

    def wait_for_sign_out_banner(self):
        self.lib.wait_for_element(self.sign_out_banner_css, By.CSS_SELECTOR)


