from selenium.webdriver.common.by import By
from Selenium_Tests.Lib.lib import Lib
from selenium.common.exceptions import NoSuchElementException


class PaymentPageMassive:

    def __init__(self, driver):
        self.driver = driver
        self.lib = Lib(driver)

    free_trial_important_button_css = "[data-test-id=\"DIALOG_BUTTON-0\"]"

    payment_methods_css = ".PaymentAccordion"

    credit_card_method_css = "div.AccordionSection:nth-child(1) > div:nth-child(1) > div:nth-child(1)"
    credit_card_number_css = "#paymentCreditCardNumber"
    credit_card_expiry_month_css = "#paymentCreditCardExpiryMonth"
    credit_card_expiry_year_css = "#paymentCreditCardExpiryYear"
    credit_card_security_code_css = "#paymentCreditCardCVV"
    credit_card_start_button_css = "button.ButtonBase:nth-child(4)"


    def credit_card_method_click(self):
        credit_card_method = self.driver.find_element_by_css_selector(self.credit_card_method_css)
        credit_card_method.click()

    def fill_card_number_field(self, text):
        card_number = self.driver.find_element_by_css_selector(self.credit_card_number_css)
        card_number.clear()
        card_number.send_keys(text)

    def fill_expiry_date_month_field(self, text):
        expiry_month = self.driver.find_element_by_css_selector(self.credit_card_expiry_month_css)
        expiry_month.send_keys(text)

    def fill_expiry_date_year_field(self, text):
        expiry_year = self.driver.find_element_by_css_selector(self.credit_card_expiry_year_css)
        expiry_year.send_keys(text)

    def fill_cvc_field(self, text):
        security_code = self.driver.find_element_by_css_selector(self.credit_card_security_code_css)
        security_code.clear()
        security_code.send_keys(text)

    def credit_card_cta_button_click(self):
        cta_button = self.driver.find_element_by_css_selector(self.credit_card_start_button_css)
        cta_button.click()

    def wait_for_page_to_be_open(self):
        self.lib.wait_for_element(self.payment_methods_css, By.CSS_SELECTOR)
        try:
            self.driver.find_element_by_css_selector(self.free_trial_important_button_css).click()
        except NoSuchElementException:
            print("The user is granted Free Trial")

    def pds2_credit_card_payment_method_flow(self, card_list):
        self.wait_for_page_to_be_open()
        self.credit_card_method_click()
        self.fill_card_number_field(card_list[0])
        self.fill_expiry_date_month_field(card_list[1])
        self.fill_expiry_date_year_field(card_list[2])
        self.fill_cvc_field(card_list[3])
        self.credit_card_cta_button_click()