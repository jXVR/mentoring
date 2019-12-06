from selenium.webdriver.common.by import By
from Selenium_Tests.Lib.lib import Lib
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

class Rails:

    def __init__(self, driver):
        self.driver = driver
        self.lib = Lib(driver)

    all_rails_collection_css = "[data-test-id=\"RAIL_COLLECTION_RAIL_WRAPPER\"]"
    single_rail_name_css = "[data-test-id=\"RAIL_TITLE\"]"

    single_tile_all_data_css = "[data-test-id=\"TILE_WRAPPER\"]"

    single_tile_name_css = "[data-test-id=\"DEFAULT_TILE_TITLE\"]"
    tiles_metadata_css = "[data-test-id=\"DEFAULT_TILE_METADATA\"]"
    tile_date_css = "[data-test-id=\"DEFAULT_TILE_DATE\"]"
    tiles_background_css = "[data-test-id=\"IMAGE_WRAPPER\"]"
    tiles_video_css = "[data-test-id=\"TILE_WRAPPER\"]"

    def print_all_tiles_name(self):
        rails_dict = {}
        all_rails_collections = self.driver.find_elements_by_css_selector(self.all_rails_collection_css)

        for rail in all_rails_collections:

            single_rail_name = rail.find_element_by_css_selector(self.single_rail_name_css)

            all_tiles_in_one_rail_names = rail.find_elements_by_css_selector(self.single_tile_name_css)

            rails_dict[single_rail_name.text] = []

            for single_tile in all_tiles_in_one_rail_names:
                rails_dict[single_rail_name.text].append(single_tile.get_attribute("innerHTML"))

        print(rails_dict)
        data = pd.DataFrame.from_dict(rails_dict, orient='index')
        transpose_data = data.transpose()
        transpose_data.to_excel("rails.xlsx")

    def print_all_rails_name_and_metadata(self, excel_name):
        rails_dict = {}
        all_rails_collections = self.driver.find_elements_by_css_selector(self.all_rails_collection_css)

        for count, rail in enumerate(all_rails_collections):

            single_rail_name = rail.find_element_by_css_selector(self.single_rail_name_css)

            every_tiles_all_data = rail.find_elements_by_css_selector(self.single_tile_all_data_css)

            rails_dict[single_rail_name.text] = []

            for single_tile in every_tiles_all_data:
                try:
                    single_tile_name = single_tile.find_element_by_css_selector(self.single_tile_name_css)
                    rails_dict[single_rail_name.text].append(single_tile_name.get_attribute("innerHTML"))
                except NoSuchElementException:
                    pass
                try:
                    single_tile_metadata = single_tile.find_element_by_css_selector(self.tiles_metadata_css)
                    rails_dict[single_rail_name.text].append(single_tile_metadata.get_attribute("innerHTML"))
                except NoSuchElementException:
                    pass
                try:
                    single_tile_data = single_tile.find_element_by_css_selector(self.tile_date_css)
                    rails_dict[single_rail_name.text].append(single_tile_data.get_attribute("innerHTML"))
                except NoSuchElementException:
                    pass
                try:
                    single_tile_background = single_tile.find_element_by_css_selector(self.tiles_background_css)
                    single_tile_background_link = single_tile_background.find_element_by_css_selector(":first-child")
                    rails_dict[single_rail_name.text].append(single_tile_background_link.get_attribute("src"))
                except NoSuchElementException:
                    pass
                try:
                    rails_dict[single_rail_name.text].append(single_tile.get_attribute("href"))
                except NoSuchElementException:
                    pass

        # print(rails_dict)
        data = pd.DataFrame.from_dict(rails_dict, orient='index')
        transpose_data = data.transpose()
        transpose_data.to_excel(f"../Output_files/{excel_name}.xlsx")

    def wait_for_page_to_be_open(self):
        self.lib.wait_for_element(self.single_rail_name_css, By.CSS_SELECTOR)


