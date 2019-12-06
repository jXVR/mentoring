from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Selenium_Tests.Lib.lib import Lib

class SportPageTiles:

    def __init__(self, driver):
        self.driver = driver
        self.lib = Lib(driver)

    tile_css = "[data-test-id=\"IMAGE_WRAPPER\"]"


    def scroll_to_element(self, competition_name):
        tile = self.driver.find_element_by_css_selector(f"[alt=\"{competition_name}\"]")
        actions = ActionChains(self.driver)
        actions.move_to_element(tile).perform()

    def click_competition_tile(self, tile_name):
        competition_tile = self.driver.find_element_by_css_selector(f"[alt=\"{tile_name}\"]")
        competition_tile.click()

    def wait_for_tiles_to_load(self):
        self.lib.wait_for_element(self.tile_css, By.CSS_SELECTOR)

    def wait_for_competitions_tiles_to_load(self, competition_name):
        self.lib.wait_for_element(f"[alt=\"{competition_name}\"]", By.CSS_SELECTOR)

    def go_to_competition_page(self, competition_name):
        self.wait_for_competitions_tiles_to_load(competition_name)
        self.scroll_to_element(competition_name)
        self.click_competition_tile(competition_name)
