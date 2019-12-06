import unittest
import time
from Selenium_Tests.Lib.lib import Lib
from Selenium_Tests.Lib.lib import select_driver
from Selenium_Tests.Pages.Login.login_page import LoginPage
from Selenium_Tests.Pages.Catalog_topbar.home_page_top_bar import HomePageTopBar
from Selenium_Tests.Pages.Catalog_pages.sports_dropdown import SportsDropdown
from Selenium_Tests.Pages.Catalog_pages.home_page_tiles import HomePageTiles
from Selenium_Tests.Pages.Catalog_pages.sport_page import SportPageTiles
from Selenium_Tests.Pages.Catalog_pages.competitions_page import CompetitionsPageTiles
from Selenium_Tests.Pages.Catalog_pages.competitor_page import CompetitorPageTiles
from Selenium_Tests.Pages.Catalog_pages.squads_page import SquadsPage


class SquadsTest(unittest.TestCase):
    driver = None
    browser = "Chrome"
    lib = None
    lp = None
    home_page = None
    sports_dropdown = None
    home_page_tiles = None
    sport_page = None
    competition_page = None
    competitor_page = None
    squads = None
    test_failed = True

    def setUp(self):
        self.driver = select_driver(self.browser)
        self.driver.set_window_size(1000, 1600)
        self.lib = Lib(self.driver)
        self.lp = LoginPage(self.driver)
        self.driver.get(self.lp.url)
        self.home_page = HomePageTopBar(self.driver)
        self.sports_dropdown = SportsDropdown(self.driver)
        self.home_page_tiles = HomePageTiles(self.driver)
        self.sport_page = SportPageTiles(self.driver)
        self.competition_page = CompetitionsPageTiles(self.driver)
        self.competitor_page = CompetitorPageTiles(self.driver)
        self.squads = SquadsPage(self.driver)
        self.test_failed = True

    def tearDown(self):
        test_name = unittest.TestCase.id(self)
        if self.test_failed:
            self.driver.save_screenshot(f"../Error_screens/{test_name}.png")
        self.driver.close()

    def test_get_players_data_from_one_club(self):
        sport = "Football"
        league = "Bundesliga"
        team = "FC Bayern München"
        self.lp.login('xpdazn+de002@gmail.com', '12345')
        self.home_page.wait_for_page_to_be_open()
        self.sports_dropdown.click_sports_button()
        self.sports_dropdown.wait_for_sport_drop_down()
        self.home_page_tiles.wait_for_tiles_to_load()
        self.sports_dropdown.select_sport_by_name(sport)
        self.sport_page.wait_for_tiles_to_load()
        self.sport_page.go_to_competition_page(league)
        self.competition_page.wait_for_tiles_to_load()
        self.competition_page.go_to_competitor_page(team)
        self.competitor_page.wait_for_page_to_load()
        self.competitor_page.click_squad()
        self.squads.wait_for_page_to_be_open()
        data = self.squads.get_players_metadata()
        self.lib.dataframes_to_excel_to_separate_sheets([data], [team], team)

        self.test_failed = False

    def test_get_players_data_from_one_league(self):
        sport = "Football"
        league = "LaLiga Santander"
        self.lp.login('xpdazn+de002@gmail.com', '12345')
        self.home_page.wait_for_page_to_be_open()
        self.sports_dropdown.click_sports_button()
        self.sports_dropdown.wait_for_sport_drop_down()
        self.home_page_tiles.wait_for_tiles_to_load()
        self.sports_dropdown.select_sport_by_name(sport)
        self.sport_page.wait_for_tiles_to_load()
        self.sport_page.go_to_competition_page(league)
        self.competition_page.wait_for_tiles_to_load()
        time.sleep(6)

        all_competitors = self.competition_page.capture_competitors_names()

        competitors_data_frames_collection = []
        for team in all_competitors:
            print(team.index, team)
            self.sports_dropdown.click_sports_button()
            self.sports_dropdown.wait_for_sport_drop_down()
            self.home_page_tiles.wait_for_tiles_to_load()
            self.sports_dropdown.select_sport_by_name(sport)
            self.sport_page.wait_for_tiles_to_load()
            self.sport_page.go_to_competition_page(league)
            self.competition_page.wait_for_tiles_to_load()
            self.competition_page.go_to_competitor_page(team)
            self.competitor_page.wait_for_page_to_load()
            self.competitor_page.click_squad()
            self.squads.wait_for_page_to_be_open()
            competitors_data_frames_collection.append(self.squads.get_players_metadata())

        self.lib.dataframes_to_excel_to_separate_sheets(competitors_data_frames_collection, all_competitors, league)

        self.test_failed = False

    if __name__ == "__main__":
        unittest.main()
