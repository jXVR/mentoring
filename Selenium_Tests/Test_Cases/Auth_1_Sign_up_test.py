import unittest
import time
from Selenium_Tests.Lib.lib import Lib
from Selenium_Tests.Lib.lib import select_driver
from Selenium_Tests.Pages.Catalog_topbar.home_page_top_bar import HomePageTopBar
from Selenium_Tests.Pages.Auth.auth_1_sign_up_page import SignUpPageMassive
from Selenium_Tests.Pages.Auth.auth_1_payment_page import PaymentPageMassive
from Selenium_Tests.Pages.Auth.auth_1_confirmation_page import ConfirmationPageMassive


class SignUpTest(unittest.TestCase):
    driver = None
    browser = "Chrome"
    lib = None
    lp = None
    rp_page = None
    su_page = None
    nu_payment_page = None
    fallback_page = None
    confirmation_page = None
    home_page = None
    test_failed = True

    def setUp(self):
        self.driver = select_driver(self.browser)
        self.driver.set_window_size(1000, 1600)
        self.lib = Lib(self.driver)
        self.su_page = SignUpPageMassive(self.driver)
        self.driver.get(self.su_page.url)
        self.nu_payment_page = PaymentPageMassive(self.driver)
        self.confirmation_page = ConfirmationPageMassive(self.driver)
        self.home_page = HomePageTopBar(self.driver)
        self.test_failed = True

    def tearDown(self):
        test_name = unittest.TestCase.id(self)
        if self.test_failed:
            self.driver.save_screenshot(f"../Error_screens/{test_name}.png")
        self.driver.close()

    def test_sign_up(self):
        uid = time.strftime("%H%M%S")
        email = f"xpdazn+jptest{uid}@gmail.com"

        self.su_page.fill_sign_up_user_details("Fraud", "fraud", email, "12345a", "12345a")
        self.nu_payment_page.pds2_credit_card_payment_method_flow(["4111111111111111", "10", "2020", "737"])
        self.confirmation_page.wait_for_page_to_be_open()
        self.confirmation_page.confirmation_button_click()
        self.home_page.wait_for_page_to_be_open()

        self.test_failed = False

    if __name__ == "__main__":
        unittest.main()


