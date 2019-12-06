from selenium.webdriver.common.by import By
from Selenium_Tests.Lib.lib import Lib
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

class SquadsPage:

    def __init__(self, driver):
        self.driver = driver
        self.lib = Lib(driver)

    page_title_css = "[data-test-id=\"SPORTSDATA_PAGE_TITLE\"]"
    player_container_css = ".card___1nzvh"
    goalkeepers_container_css = "[data-test-id=\"PLAYERS-GOALKEEPERS\"]"
    defenders_container_css = "[data-test-id=\"PLAYERS-DEFENCE\"]"
    midfielders_container_css = "[data-test-id=\"PLAYERS-MIDFIELD\"]"
    forwards_container_css = "[data-test-id=\"PLAYERS-FORWARDS\"]"

    player_first_name_css = "[data-test-id=\"FIRSTNAME\"]"
    player_last_name_css = "[data-test-id=\"LASTNAME\"]"
    player_age_css = "[data-test-id=\"age-value\"]"
    player_height_css = "[data-test-id=\"height-value\"]"
    player_foot_css = "[data-test-id=\"foot-value\"]"
    player_nationality_css = "[data-test-id=\"nationality-value\"]"

    player_photo_css = ".details___2auMB > :first-child > :first-child"

    def get_players_metadata(self):
        players_dict = {}
        team_name = self.driver.find_element_by_css_selector(self.page_title_css).get_attribute("innerHTML")

        all_goalkeepers_container = self.driver.find_element_by_css_selector(self.goalkeepers_container_css)
        all_goalkeepers_data = all_goalkeepers_container.find_elements_by_css_selector(self.player_container_css)

        all_defenders_container = self.driver.find_element_by_css_selector(self.defenders_container_css)
        all_defenders_data = all_defenders_container.find_elements_by_css_selector(self.player_container_css)

        all_midfielders_container = self.driver.find_element_by_css_selector(self.midfielders_container_css)
        all_midfielders_data = all_midfielders_container.find_elements_by_css_selector(self.player_container_css)

        all_forwards_container = self.driver.find_element_by_css_selector(self.forwards_container_css)
        all_forwards_data = all_forwards_container.find_elements_by_css_selector(self.player_container_css)

        for goalkeeper in all_goalkeepers_data:
            try:
                player_first_name = goalkeeper.find_element_by_css_selector(self.player_first_name_css).get_attribute("innerHTML")
            except NoSuchElementException:
                player_first_name = ""
            try:
                player_last_name = goalkeeper.find_element_by_css_selector(self.player_last_name_css).get_attribute("innerHTML")
            except NoSuchElementException:
                player_last_name = ""
            player_age = goalkeeper.find_element_by_css_selector(self.player_age_css).get_attribute("innerHTML")
            player_height = goalkeeper.find_element_by_css_selector(self.player_height_css).get_attribute("innerHTML")
            player_foot = goalkeeper.find_element_by_css_selector(self.player_foot_css).get_attribute("innerHTML")
            player_nationality = goalkeeper.find_element_by_css_selector(self.player_nationality_css).get_attribute("innerHTML")
            try:
                player_photo = goalkeeper.find_element_by_css_selector(self.player_photo_css).get_attribute("src")
            except NoSuchElementException:
                player_photo = ""

            players_dict[f"{player_first_name} {player_last_name}"] = [int(player_age), player_height, player_foot, player_nationality, player_photo]

        for defender in all_defenders_data:
            try:
                player_first_name = defender.find_element_by_css_selector(self.player_first_name_css).get_attribute("innerHTML")
            except NoSuchElementException:
                player_first_name = ""
            try:
                player_last_name = defender.find_element_by_css_selector(self.player_last_name_css).get_attribute("innerHTML")
            except NoSuchElementException:
                player_last_name = ""
            player_age = defender.find_element_by_css_selector(self.player_age_css).get_attribute("innerHTML")
            player_height = defender.find_element_by_css_selector(self.player_height_css).get_attribute("innerHTML")
            player_foot = defender.find_element_by_css_selector(self.player_foot_css).get_attribute("innerHTML")
            player_nationality = defender.find_element_by_css_selector(self.player_nationality_css).get_attribute("innerHTML")
            try:
                player_photo = defender.find_element_by_css_selector(self.player_photo_css).get_attribute("src")
            except NoSuchElementException:
                player_photo = ""

            players_dict[f"{player_first_name} {player_last_name}"] = [int(player_age), player_height, player_foot, player_nationality, player_photo]

        for midfielder in all_midfielders_data:
            try:
                player_first_name = midfielder.find_element_by_css_selector(self.player_first_name_css).get_attribute("innerHTML")
            except NoSuchElementException:
                player_first_name = ""
            try:
                player_last_name = midfielder.find_element_by_css_selector(self.player_last_name_css).get_attribute("innerHTML")
            except NoSuchElementException:
                player_last_name = ""
            player_age = midfielder.find_element_by_css_selector(self.player_age_css).get_attribute("innerHTML")
            player_height = midfielder.find_element_by_css_selector(self.player_height_css).get_attribute("innerHTML")
            player_foot = midfielder.find_element_by_css_selector(self.player_foot_css).get_attribute("innerHTML")
            player_nationality = midfielder.find_element_by_css_selector(self.player_nationality_css).get_attribute("innerHTML")
            try:
                player_photo = midfielder.find_element_by_css_selector(self.player_photo_css).get_attribute("src")
            except NoSuchElementException:
                player_photo = ""

            players_dict[f"{player_first_name} {player_last_name}"] = [int(player_age), player_height, player_foot, player_nationality, player_photo]

        for forward in all_forwards_data:
            try:
                player_first_name = forward.find_element_by_css_selector(self.player_first_name_css).get_attribute("innerHTML")
            except NoSuchElementException:
                player_first_name = ""
            try:
                player_last_name = forward.find_element_by_css_selector(self.player_last_name_css).get_attribute("innerHTML")
            except NoSuchElementException:
                player_last_name = ""
            player_age = forward.find_element_by_css_selector(self.player_age_css).get_attribute("innerHTML")
            player_height = forward.find_element_by_css_selector(self.player_height_css).get_attribute("innerHTML")
            player_foot = forward.find_element_by_css_selector(self.player_foot_css).get_attribute("innerHTML")
            player_nationality = forward.find_element_by_css_selector(self.player_nationality_css).get_attribute("innerHTML")
            try:
                player_photo = forward.find_element_by_css_selector(self.player_photo_css).get_attribute("src")
            except NoSuchElementException:
                player_photo = ""

            players_dict[f"{player_first_name} {player_last_name}"] = [int(player_age), player_height, player_foot, player_nationality, player_photo]

        # print(players_dict)

        data = pd.DataFrame.from_dict(players_dict, orient='index')
        # transpose_data = data.transpose()
        # data.to_excel(f"{team_name}.xlsx", sheet_name=f'{team_name}',
        #               header= ["Age", "Height", "Foot", "Nationality", "Photo URL"],
        #               index_label="Name")
        return data


    def wait_for_page_to_be_open(self):
        self.lib.wait_for_element(self.page_title_css, By.CSS_SELECTOR)