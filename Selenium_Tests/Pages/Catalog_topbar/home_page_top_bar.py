from selenium.webdriver.common.by import By
from Selenium_Tests.Lib.lib import Lib

class HomePageTopBar:

    def __init__(self, driver):
        self.driver = driver
        self.lib = Lib(driver)

    home_page_header_nav_item = "[data-test-id=\"HEADER_NAVIGATION_ITEM_LINK\"]"
    dazn_logo_css = ".logo___logo___3BUpT"
    home_css = ".header-nav___left-nav___2-Pp3 > li:nth-child(1) > a:nth-child(1)"
    schedule_css = ".header-nav___left-nav___2-Pp3 > li:nth-child(2) > a:nth-child(1)"
    sports_css = ".header-nav___left-nav___2-Pp3 > li:nth-child(3) > button:nth-child(1)"
    menu_css = ".header-nav___right-nav___3eW6Q > li:nth-child(1) > button:nth-child(1)"
    search_css = "[data-test-id=\"NAVIGATION_SEARCH_ICON_OPEN\"]"

    tile_css = "[data-test-id=\"IMAGE_WRAPPER\"]"



    # jak przerobic cssy?
    # czy do css selectora jako parametr da sie dodac inner text / xpath / jak to zrobic

    def click_dazn_logo(self):
        dazn_logo = self.driver.find_element_by_css_selector(self.dazn_logo_css)
        dazn_logo.click()

    def click_home(self):
        home = self.driver.find_element_by_css_selector(self.home_css)
        home.click()

    def click_schedule(self):
        schedule = self.driver.find_element_by_css_selector(self.schedule_css)
        schedule.click()

    def click_sports_dropdown(self):
        sports_dropdown = self.driver.find_element_by_css_selector(self.sports_css)
        sports_dropdown.click()

    def click_menu_dropdown(self):
        menu_dropdown = self.driver.find_element_by_css_selector(self.menu_css)
        menu_dropdown.click()

    def click_search(self):
        search = self.driver.find_element_by_css_selector(self.search_css)
        search.click()

    def wait_for_page_to_be_open(self):
        self.lib.wait_for_element(self.home_page_header_nav_item, By.CSS_SELECTOR)
