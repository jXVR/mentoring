from Selenium_Tests.Lib.lib import Lib
from selenium.webdriver.common.by import By

class SportsDropdown:
    def __init__(self, driver):
        self.driver = driver
        self.lib = Lib(driver)

    # Selector
    sports_button_css = ".header-nav___left-nav___2-Pp3 > li:nth-child(3) > button:nth-child(1)"
    sports_page_header_css = "[data-test-id=\"PAGE_TITLE\"]"

    single_sport_in_sport_list = "[data-test-id=\"SPORTS-MENU-LIST-ITEM\"]"
    sports_dropdown_container = "[data-test-id=\"SPORTS-MENU-DROPDOWN\"] > *"

    # Actions
    def click_sports_button(self):
        sports_button = self.driver.find_element_by_css_selector(self.sports_button_css)
        sports_button.click()

    def select_sport(self, number):
        all_sports_list = self.driver.find_elements_by_css_selector(self.sports_dropdown_container)
        element = all_sports_list[number].find_element_by_css_selector(self.single_sport_in_sport_list)
        element.click()

    def wait_for_sport_drop_down(self):
        self.lib.wait_for_element(self.single_sport_in_sport_list, By.CSS_SELECTOR)

    def wait_for_sport_page(self):
        self.lib.wait_for_element(self.sports_page_header_css, By.CSS_SELECTOR)

    def select_sport_by_name(self, name):
        sports = self.driver.find_element_by_css_selector(self.sports_dropdown_container)
        # for sport in sports:
        #     if sport.text == name:
        #         selected_sport = sport.find_element_by_css_selector(self.single_sport_in_sport_list)
        #         selected_sport.click()
        #         break

        any_sport_button_css = f"[title=\"{name}\"]"
        sport = sports.find_element_by_css_selector(any_sport_button_css)
        sport.click()


