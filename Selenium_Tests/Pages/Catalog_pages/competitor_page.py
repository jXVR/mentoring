from selenium.webdriver.common.by import By
from Selenium_Tests.Lib.lib import Lib

class CompetitorPageTiles:

    def __init__(self, driver):
        self.driver = driver
        self.lib = Lib(driver)

    squad_css = "[data-test-id=\"SQUADS_BUTTON\"]"
    tile_css = "[data-test-id=\"IMAGE_WRAPPER\"]"

    def click_squad(self):
        squad = self.driver.find_element_by_css_selector(self.squad_css)
        squad.click()

    def wait_for_tiles_to_load(self):
        self.lib.wait_for_element(self.tile_css, By.CSS_SELECTOR)

    def wait_for_page_to_load(self):
        self.lib.wait_for_element(self.squad_css, By.CSS_SELECTOR)
