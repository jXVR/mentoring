import unittest
import time
from Selenium_Tests.Lib.lib import Lib
from Selenium_Tests.Lib.lib import select_driver
from Selenium_Tests.Pages.Login.login_page import LoginPage
from Selenium_Tests.Pages.Catalog_topbar.home_page_top_bar import HomePageTopBar
from Selenium_Tests.Pages.Catalog_pages.schedule_page import SchedulePage
from Selenium_Tests.Pages.Catalog_pages.sports_dropdown import SportsDropdown
from Selenium_Tests.Pages.Catalog_topbar.menu_dropdown import MenuDropdown
from Selenium_Tests.Pages.Catalog_pages.search_page import SearchPage

# porozbijac  testy na poszczegolne pliki zeby zrobic suite

class HomePageTest(unittest.TestCase):
    driver = None
    browser = "Chrome"
    lib = None
    lp = None
    home_page = None
    schedule_page = None
    sports_dropdown = None
    menu_dropdown = None
    search_page = None
    test_failed = True


    def setUp(self):
        self.driver = select_driver(self.browser)
        self.driver.set_window_size(1000, 1600)
        self.lib = Lib(self.driver)
        self.lp = LoginPage(self.driver)
        self.driver.get(self.lp.url)
        self.home_page = HomePageTopBar(self.driver)
        self.schedule_page = SchedulePage(self.driver)
        self.sports_dropdown = SportsDropdown(self.driver)
        self.menu_dropdown = MenuDropdown(self.driver)
        self.search_page = SearchPage(self.driver)
        self.test_failed = True

    def tearDown(self):
        test_name = unittest.TestCase.id(self)
        if self.test_failed:
            self.driver.save_screenshot(f"../Error_screens/{test_name}.png")
        self.driver.close()

    def test_hompe_page_crawler(self):
        self.lp.login('xpdazn+de002@gmail.com', '12345')
        self.home_page.wait_for_page_to_be_open()
        self.assertTrue(self.driver.find_element_by_css_selector('.header-nav___active___29uvE').is_displayed(),
                        "Home page is not open")

        self.sports_dropdown.click_sports_button()
        self.sports_dropdown.wait_for_sport_drop_down()
        self.sports_dropdown.select_sport(5)
        self.sports_dropdown.wait_for_sport_page()
        # time.sleep(2)

        self.home_page.click_dazn_logo()
        self.home_page.wait_for_page_to_be_open()
        # time.sleep(2)

        self.sports_dropdown.click_sports_button()
        self.sports_dropdown.wait_for_sport_drop_down()
        self.sports_dropdown.select_sport_by_name("Football")
        self.sports_dropdown.wait_for_sport_page()
        # time.sleep(2)

        self.home_page.click_home()
        self.home_page.wait_for_page_to_be_open()
        # time.sleep(2)

        self.home_page.click_search()
        self.search_page.wait_for_page_to_be_open()
        # time.sleep(2)

        self.home_page.click_schedule()
        self.schedule_page.wait_for_page_to_be_open()
        # time.sleep(2)

        ### Not working because of Help 2.0 has been released to DE STAG and PROD

        # self.home_page.click_menu_dropdown()
        # self.menu_dropdown.click_help_button()
        # time.sleep(6)

        # self.menu_dropdown.click_dazn_logo_on_help_page()
        # self.home_page.wait_for_page_to_be_open()

        self.home_page.click_menu_dropdown()
        self.menu_dropdown.click_sign_out_button()
        self.menu_dropdown.wait_for_sign_out_banner()
        self.menu_dropdown.click_sign_out_cancelation()
        time.sleep(2)

        self.home_page.click_menu_dropdown()
        self.menu_dropdown.click_sign_out_button()
        self.menu_dropdown.click_sign_out_confirmation()
        time.sleep(10)

        self.test_failed = False

    def test_schedule_crawler(self):
        self.lp.login('xpdazn+de002@gmail.com', '12345')
        self.home_page.wait_for_page_to_be_open()

        self.home_page.click_schedule()
        self.schedule_page.wait_for_page_to_be_open()

        self.schedule_page.make_max_past_date_visible()
        self.schedule_page.max_past_date_tile_click()
        time.sleep(3)

        self.schedule_page.make_max_future_date_visible()
        self.schedule_page.max_future_date_tile_click()
        time.sleep(2)

        self.schedule_page.make_today_date_visible()
        self.schedule_page.today_date_tile_click()
        time.sleep(2)

        self.test_failed = False

    if __name__ == "__main__":
        unittest.main()


