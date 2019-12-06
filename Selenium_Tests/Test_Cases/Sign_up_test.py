import unittest
import time
from Selenium_Tests.Lib.lib import Lib
from Selenium_Tests.Lib.lib import select_driver
from Selenium_Tests.Pages.Login.login_page import LoginPage
from Selenium_Tests.Pages.Catalog_topbar.home_page_top_bar import HomePageTopBar
from Selenium_Tests.Pages.Login.rate_plans_page import RatePlansPage
from Selenium_Tests.Pages.Auth_2_PSD2.pds2_sign_up_page import SignUpPage
from Selenium_Tests.Pages.Auth_2_PSD2.psd2_payment_page import PaymentPage
from Selenium_Tests.Pages.Auth_2_PSD2.pds2_3ds1_redirection_page import FallbackPage
from Selenium_Tests.Pages.Auth_2_PSD2.confirmation_page import ConfirmationPage
from random import choice
from Selenium_Tests.Lib.constant import credit_cards_3ds1_dict as cc_type


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
        self.lp = LoginPage(self.driver)
        self.rp_page = RatePlansPage(self.driver)
        self.driver.get(self.rp_page.url)
        self.driver.execute_script("window.localStorage.setItem('Auth_2_PSD2', true)")
        self.su_page = SignUpPage(self.driver)
        self.nu_payment_page = PaymentPage(self.driver)
        self.fallback_page = FallbackPage(self.driver)
        self.confirmation_page = ConfirmationPage(self.driver)
        self.home_page = HomePageTopBar(self.driver)
        self.test_failed = True

    def tearDown(self):
        test_name = unittest.TestCase.id(self)
        if self.test_failed:
            self.driver.save_screenshot(f"../Error_screens/{test_name}.png")
        self.driver.close()

    def test_sign_up(self):
        uid = time.strftime("%H%M%S")
        email = f"xpdazn+brfe{uid}@gmail.com"
        cc_name = choice(list(cc_type))
        print(email, cc_type[cc_name][0], cc_name)
        self.rp_page.wait_for_page_to_be_open()
        self.lp.cookie_button_click()
        # self.driver.execute_script("window.localStorage.setItem('Auth_2_PSD2', true)")
        self.rp_page.monthly_plan_click()
        self.su_page.fill_sign_up_user_details("Fraud", "fraud", email, email, "12345a")
        self.nu_payment_page.pds2_credit_card_payment_method_flow(cc_type[cc_name])
        self.fallback_page.complete_fallback_scenario("user", "password")
        self.lib.get_correlation_id()
        time.sleep(5)
        self.confirmation_page.wait_for_page_to_be_open()
        self.lib.get_correlation_id()
        time.sleep(5)
        self.confirmation_page.confirmation_button_click()
        time.sleep(3)

        self.test_failed = False

    if __name__ == "__main__":
        unittest.main()


