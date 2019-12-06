from Selenium_Tests.Lib.lib import Lib
from selenium.webdriver.common.by import By
import time

class SchedulePage:
    def __init__(self, driver):
        self.driver = driver
        self.lib = Lib(driver)

    filter_sport_css = "[data-test-id=\"SPORTFILTER_BUTTON\"]"
    every_sport_item_css = "[data-test-id=\"SPORT_FILTER_ITEM\"]"
    reset_sport_filter_css = "[data-test-id=\"RESET_SPORT_FILTERS\"]"
    sports_filter_count_css = "[data-test-id=\"SPORT_FILTER_COUNT\"]"
    # sporty po xpathie


    today_date_tile_css = "[data-test-id=\"DATETILE_TILE DATETILE_TODAY\"]"

    any_date_tile_css = "[data-test-id=\"DATETILE_TILE\"]"


    date_scroller_forward_arrow_css = "[data-test-id=\"DATE_SCROLLER_FORWARD_ARROW\"]"
    date_scroller_back_arrow_css = "[data-test-id=\"DATE_SCROLLER_BACK_ARROW\"]"


    dates_container_css = ".date-scroller___date-scroller___2luAU > div:nth-child(1) > div:nth-child(1) > *"
    first_date_css = "div.date-tile___date-tile___2wXId:nth-child(1)"
    last_date_css = "div.date-tile___date-tile___2wXId:last-child"
    # div, li, roznice
    # problem ze zbudowaniem listy i znalezieniem ostatniego elementu tej listy


    def date_scroller_forward_click(self):
        date_scroller_forward = self.driver.find_element_by_css_selector(self.date_scroller_forward_arrow_css)
        date_scroller_forward.click()

    def date_scroller_back_click(self):
        date_scroller_back = self.driver.find_element_by_css_selector(self.date_scroller_back_arrow_css)
        date_scroller_back.click()

    def today_date_tile_click(self):
        today_date = self.driver.find_element_by_css_selector(self.today_date_tile_css)
        today_date.click()

    # def max_future_date_tile_click(self):
    #     all_dates_list = self.driver.find_elements_by_css_selector(self.dates_container_css)
    #     max_future_date_tile = all_dates_list[0].find_element_by_css_selector(self.any_date_tile_css)
    #     max_future_date_tile.click()
    #
    # def max_past_date_tile_click(self):
    #     all_dates_list = self.driver.find_elements_by_css_selector(self.dates_container_css)
    #     max_past_date_tile = all_dates_list[-1].find_element_by_css_selector(self.any_date_tile_css)
    #     max_past_date_tile.click()

    def max_future_date_tile_click(self):
        max_future_date_tile = self.driver.find_element_by_css_selector(self.last_date_css)
        max_future_date_tile.click()

    def max_past_date_tile_click(self):
        max_past_date_tile = self.driver.find_element_by_css_selector(self.first_date_css)
        max_past_date_tile.click()

    # czy mozna to uproscic, wyczyscic, jest funkcja w funkcji
    def make_max_future_date_visible(self):
        while not self.driver.find_element_by_css_selector(self.last_date_css).is_displayed():
            self.date_scroller_forward_click()
            time.sleep(1)

    def make_max_past_date_visible(self):
        while not self.driver.find_element_by_css_selector(self.first_date_css).is_displayed():
            self.date_scroller_back_click()
            time.sleep(1)

    # jak uniezaleznic to od strony od ktorej zaczynamy / past / forward
    def make_today_date_visible(self):
        while not self.driver.find_element_by_css_selector(self.today_date_tile_css).is_displayed():
            self.date_scroller_back_click()
            time.sleep(1)

    def wait_for_page_to_be_open(self):
        self.lib.wait_for_element(self.filter_sport_css, By.CSS_SELECTOR)
