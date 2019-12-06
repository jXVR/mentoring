from selenium.webdriver.common.by import By
from Selenium_Tests.Lib.lib import Lib


class RatePlansPage:
    url = "https://stag.dazn.com/de-DE/account/payment-plan"

    def __init__(self, driver):
        self.driver = driver
        self.lib = Lib(driver)

    rate_plan_tile_css = "[data-test-id=\"plan-details__title\"]"

    annual_rate_plan_button_css = "[data-test-id=\"plan-details__wrapper_Annual\"]"
    monthly_rate_plan_button_css = "[data-test-id=\"plan-details__wrapper_Month\"]"

    def annual_plan_click(self):
        annual_button_click = self.driver.find_element_by_css_selector(self.annual_rate_plan_button_css)
        annual_button_click.click()

    def monthly_plan_click(self):
        monthly_button_click = self.driver.find_element_by_css_selector(self.monthly_rate_plan_button_css)
        monthly_button_click.click()

    def wait_for_page_to_be_open(self):
        self.lib.wait_for_element(self.rate_plan_tile_css, By.CSS_SELECTOR)

    # funkcja na wybor rate planu powinna uwzgledniac cookiebanner, czy przerzucac go do Lib,
    # tak samo jak language switcher czy przerzucic do lib i jak / automatyczne wybranie drugiego jezyka