from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Selenium_Tests.Lib.lib import Lib

class CompetitionsPageTiles:

    def __init__(self, driver):
        self.driver = driver
        self.lib = Lib(driver)

    tile_css = "[data-test-id=\"IMAGE_WRAPPER\"]"
    competitors_container_css = "[data-test-id=\"rail-Competitors\"]"
    competitor_name_css = "[data-test-id=\"DEFAULT_TILE_TITLE\"]"


    def scroll_to_element(self, competitor_name):
        tile = self.driver.find_element_by_css_selector(f"[alt=\"{competitor_name}\"]")
        actions = ActionChains(self.driver)
        actions.move_to_element(tile).perform()

    def click_competitor_tile(self, tile_name):
        competitor_tile = self.driver.find_element_by_css_selector(f"[alt=\"{tile_name}\"]")
        competitor_tile.click()

    def wait_for_tiles_to_load(self):
        self.lib.wait_for_element(self.tile_css, By.CSS_SELECTOR)

    def wait_for_competitors_tiles_to_load(self, competitor_name):
        self.lib.wait_for_element(f"[alt=\"{competitor_name}\"]", By.CSS_SELECTOR)

    def capture_competitors_names(self):
        competitors_rail = self.driver.find_element_by_css_selector(self.competitors_container_css)
        names = competitors_rail.find_elements_by_css_selector(self.competitor_name_css)
        names_list = []
        for team in names:
            names_list.append(team.get_attribute("innerHTML"))
        print(names_list)
        return names_list

    def go_to_competitor_page(self, competitor_name):
        self.wait_for_competitors_tiles_to_load(competitor_name)
        self.scroll_to_element(competitor_name)
        self.click_competitor_tile(competitor_name)
