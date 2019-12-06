from selenium.webdriver.common.by import By
from Selenium_Tests.Lib.lib import Lib
from selenium.common.exceptions import NoSuchElementException
import time


class PaymentPage:

    def __init__(self, driver):
        self.driver = driver
        self.lib = Lib(driver)

    free_trial_important_button_css = "[data-test-id=\"DIALOG_BUTTON-0\"]"

    payment_methods_css = "[data-test-id=\"select-payment__options\"]"
    change_payment_method_css = "[data-test-id=\"select-payment__change-subscription-button\"]"
    direct_debit_method_css = "[data-test-id=\"select-payment__option__DirectDebit_Button\"]"
    account_name_css = "[data-test-id=\"ACCOUNT_NAME\"]"
    iban_css = "[data-test-id=\"IBAN\"]"
    iban_start_button_css = "[data-test-id=\"DIRECTDEBIT_PAYMENT_BUTTON\"]"

    # Auth 2.0
    credit_card_method_css = "[data-test-id=\"select-payment__option__CreditCard\"]"
    credit_card_number_css = "[data-test-id=\"CREDIT_CARD_NUMBER\"]"
    credit_card_expiry_month_css = "[data-test-id=\"EXPIRY_DATE-0\"]"
    credit_card_expiry_year_css = "[data-test-id=\"EXPIRY_DATE-1\"]"
    credit_card_security_code_css = "[data-test-id=\"SECURITY_CODE\"]"
    credit_card_start_button_css = "[data-test-id=\"CREDITCARD_PAYMENT_BUTTON\"]"

    # Auth_2_PSD2 fields
    iframes_class_name = "js-iframe"

    credit_card_method_pds2_css = "[data-test-id=\"select-payment__option__CreditCard_Button\"]"

    card_number_psd2_iframe_css = "[data-cse=\"encryptedCardNumber\"]"
    card_number_psd2_fill_css = '[aria-label=\"Credit or debit card number\"]'

    expiry_date_month_psd2_iframe_css = "[data-cse=\"encryptedExpiryMonth\"]"
    expiry_date_month_psd2_fill_css = "[aria-label=\"Credit or debit card expiration month - 2 digits\"]"
    expiry_date_year_psd2_iframe_css = "[data-cse=\"encryptedExpiryYear\"]"
    expiry_date_year_psd2_fill_css = "[aria-label=\"Credit or debit card expiration year - 2 digits\"]"
    security_code_psd2_iframe_css = "[data-cse=\"encryptedSecurityCode\"]"
    security_code_psd2_fill_css = "[aria-label=\"Credit or debit card 3 or 4 digit security code\"]"

    # card_number_psd2_css = "div.field___field___2-rqv:nth-child(2) > div:nth-child(1) > div:nth-child(2)"
    # expiry_date_month_css = "div.field___field___2-rqv:nth-child(3) > div:nth-child(1) > div:nth-child(2)"
    # expiry_date_year_css = "div.field___field___2-rqv:nth-child(3) > div:nth-child(1) > div:nth-child(2)"
    # security_code_css = "div.field___field___2-rqv:nth-child(4) > div:nth-child(1) > div:nth-child(2)"
    street_adress_css = "div.field___field___Q96I_:nth-child(5) > div:nth-child(1) > input:nth-child(2)"
    house_number_css = "div.field___field___Q96I_:nth-child(6) > div:nth-child(1) > input:nth-child(2)"
    postal_code_css = "div.field___field___Q96I_:nth-child(7) > div:nth-child(1) > input:nth-child(2)"
    city_css = "div.field___field___Q96I_:nth-child(8) > div:nth-child(1) > input:nth-child(2)"
    credit_card_psd2_start_button_css = "button.button___button___3oHbw:nth-child(6)"

    paypal_method_css = "[data-test-id=\"select-payment__option__PayPal\"]"
    paypal_start_button_css = ".paymentDetails___paypal-button___XE9Ml"

    gift_code_method_css = "[data-test-id=\"select-payment__giftcode\"]"
    gift_code_field_css = "[data-test-id=\"GIFT_CODE\"]"
    gift_code_start_button_css = "[data-test-id=\"select-payment__giftcode-redeem-button\"]"



    def change_subscription_on_payment_details_page_click(self):
        change_subscription = self.driver.find_element_by_css_selector(self.change_payment_method_css)
        change_subscription.click()

    def direct_debit_method_click(self):
        direct_debit_method = self.driver.find_element_by_css_selector(self.direct_debit_method_css)
        direct_debit_method.click()


    def credit_card_method_click(self):
        credit_card_method = self.driver.find_element_by_css_selector(self.credit_card_method_css)
        credit_card_method.click()

    def pds2_select_credit_card_method_click(self):
        credit_card_method = self.driver.find_element_by_css_selector(self.credit_card_method_pds2_css)
        credit_card_method.click()

    def psd2_fill_card_number_field(self, text):
        self.lib.wait_for_element(self.card_number_psd2_iframe_css, By.CSS_SELECTOR)
        element = self.driver.find_element_by_css_selector(self.card_number_psd2_iframe_css)
        iframe = element.find_element_by_class_name(self.iframes_class_name)
        self.driver.switch_to.frame(iframe)
        card_number = self.driver.find_element_by_css_selector(self.card_number_psd2_fill_css)
        card_number.clear()
        card_number.send_keys(text)
        self.driver.switch_to.default_content()

    def psd2_fill_expiry_date_month_field(self, text):
        self.lib.wait_for_element(self.expiry_date_month_psd2_iframe_css, By.CSS_SELECTOR)
        element = self.driver.find_element_by_css_selector(self.expiry_date_month_psd2_iframe_css)
        iframe = element.find_element_by_class_name(self.iframes_class_name)
        self.driver.switch_to.frame(iframe)
        expiry_month = self.driver.find_element_by_css_selector(self.expiry_date_month_psd2_fill_css)
        expiry_month.clear()
        expiry_month.send_keys(text)
        self.driver.switch_to.default_content()

    def psd2_fill_expiry_date_year_field(self, text):
        self.lib.wait_for_element(self.expiry_date_year_psd2_iframe_css, By.CSS_SELECTOR)
        element = self.driver.find_element_by_css_selector(self.expiry_date_year_psd2_iframe_css)
        iframe = element.find_element_by_class_name(self.iframes_class_name)
        self.driver.switch_to.frame(iframe)
        expiry_year = self.driver.find_element_by_css_selector(self.expiry_date_year_psd2_fill_css)
        expiry_year.clear()
        expiry_year.send_keys(text)
        self.driver.switch_to.default_content()

    def psd2_fill_cvc_field(self, text):
        self.lib.wait_for_element(self.security_code_psd2_iframe_css, By.CSS_SELECTOR)
        element = self.driver.find_element_by_css_selector(self.security_code_psd2_iframe_css)
        iframe = element.find_element_by_class_name(self.iframes_class_name)
        self.driver.switch_to.frame(iframe)
        security_code = self.driver.find_element_by_css_selector(self.security_code_psd2_fill_css)
        security_code.clear()
        security_code.send_keys(text)
        self.driver.switch_to.default_content()

    def psd2_fill_street_address_field(self, text):
        street_address = self.driver.find_element_by_css_selector(self.street_adress_css)
        street_address.clear()
        street_address.send_keys(text)

    def psd2_fill_house_number_field(self, text):
        house_number = self.driver.find_element_by_css_selector(self.house_number_css)
        house_number.clear()
        house_number.send_keys(text)

    def psd2_fill_postal_code_field(self, text):
        postal_code = self.driver.find_element_by_css_selector(self.postal_code_css)
        postal_code.clear()
        postal_code.send_keys(text)

    def psd2_fill_city_field(self, text):
        city = self.driver.find_element_by_css_selector(self.city_css)
        city.clear()
        city.send_keys(text)

    def psd2_credit_card_cta_button_click(self):
        cta_button = self.driver.find_element_by_css_selector(self.credit_card_psd2_start_button_css)
        cta_button.click()

    def paypal_method_click(self):
        paypal_method = self.driver.find_element_by_css_selector(self.payment_methods_css)
        paypal_method.click()

    def gift_code_method_click(self):
        gift_code_method = self.driver.find_element_by_css_selector(self.gift_code_method_css)
        gift_code_method.click()

    def wait_for_page_to_be_open(self):
        self.lib.wait_for_element(self.payment_methods_css, By.CSS_SELECTOR)
        try:
            self.driver.find_element_by_css_selector(self.free_trial_important_button_css).click()
            print("The user already had Free Trial")
        except NoSuchElementException:
            print("The user is granted Free Trial")

    def psd2_wait_for_adyen_script_to_load(self):
        self.lib.wait_for_element(self.iframes_class_name, By.CLASS_NAME)


        # time.sleep(3)

    def pds2_credit_card_payment_method_flow(self, card_list):
        self.wait_for_page_to_be_open()
        self.pds2_select_credit_card_method_click()
        self.psd2_wait_for_adyen_script_to_load()
        time.sleep(4)
        self.psd2_fill_card_number_field(card_list[0])
        time.sleep(2)
        self.psd2_fill_expiry_date_month_field(card_list[1])
        time.sleep(2)
        self.psd2_fill_expiry_date_year_field(card_list[2])
        time.sleep(2)
        self.psd2_fill_cvc_field(card_list[3])
        # self.psd2_fill_street_address_field("Street")
        # self.psd2_fill_house_number_field("House")
        # self.psd2_fill_postal_code_field("Postal Code")
        # self.psd2_fill_city_field("City")
        self.psd2_credit_card_cta_button_click()