from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Selenium_Tests.Lib.lib import Lib

class HomePageTiles:

    def __init__(self, driver):
        self.driver = driver
        self.lib = Lib(driver)

    tile_css = "[data-test-id=\"IMAGE_WRAPPER\"]"


    def scroll_to_element(self, sport_name):
        tile = self.driver.find_element_by_css_selector(f"[alt=\"{sport_name}\"]")
        actions = ActionChains(self.driver)
        actions.move_to_element(tile).perform()

    def click_all_sports_tile(self, tile_name):
        all_sports_tile = self.driver.find_element_by_css_selector(f"[alt=\"{tile_name}\"]")
        all_sports_tile.click()

    def wait_for_tiles_to_load(self):
        self.lib.wait_for_element(self.tile_css, By.CSS_SELECTOR)

    def wait_for_sports_tiles_to_load(self, sport_name):
        self.lib.wait_for_element(f"[alt=\"{sport_name}\"]", By.CSS_SELECTOR)

    def go_to_sport_page(self, sport_name):
        self.wait_for_sports_tiles_to_load(sport_name)
        self.scroll_to_element(sport_name)
        self.click_all_sports_tile(sport_name)
