import unittest
from Selenium_Tests.Lib.lib import Lib
from Selenium_Tests.Lib.lib import select_driver
from Selenium_Tests.Pages.Login.login_page import LoginPage
from Selenium_Tests.Pages.Catalog_topbar.home_page_top_bar import HomePageTopBar

class LoginTest(unittest.TestCase):
    driver = None
    browser = "Chrome"
    lib = None
    lp = None
    home_page = None
    test_failed = True

    def setUp(self):
        self.driver = select_driver(self.browser)
        self.driver.set_window_size(1000, 1600)
        self.lib = Lib(self.driver)
        self.lp = LoginPage(self.driver)
        self.driver.get(self.lp.url)
        self.home_page = HomePageTopBar(self.driver)
        self.test_failed = True

    def tearDown(self):
        test_name = unittest.TestCase.id(self)
        if self.test_failed:
            self.driver.save_screenshot(f"../Error_screens/{test_name}.png")
        self.driver.close()

    def test_correct_login_pop(self):
        self.lp.login('xpdazn+de002@gmail.com', '12345')
        self.home_page.wait_for_page_to_be_open()

        self.test_failed = False

    def test_login_with_switched_language(self):
        self.lp.switch_region("es")
        self.lp.wait_for_page_to_be_open()
        self.lp.login('xpdazn+de002@gmail.com', '12345')
        self.home_page.wait_for_page_to_be_open()

        self.test_failed = False

    if __name__ == "__main__":
        unittest.main()


