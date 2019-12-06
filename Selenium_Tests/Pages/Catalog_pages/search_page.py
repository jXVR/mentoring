from Selenium_Tests.Lib.lib import Lib
from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.lib = Lib(driver)

    search_field_css = "[data-test-id=\"SEARCH_INPUT\"]"

    def wait_for_page_to_be_open(self):
        self.lib.wait_for_element(self.search_field_css, By.CSS_SELECTOR)