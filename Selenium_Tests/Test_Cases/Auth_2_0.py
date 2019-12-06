import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginTest(unittest.TestCase):
    driver = None

    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        self.driver.get("https://stag.dazn.com")

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()

    def wait_for_element(self, selector, by):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, selector)))


    def test_sign_in_logo(self):
        self.wait_for_element('.linkButton > p:nth-child(1) > a:nth-child(2)', By.CSS_SELECTOR).click()
        self.wait_for_element('.logo___logo___31Nf0', By.CSS_SELECTOR).click()
        self.assertTrue(self.driver.find_element_by_css_selector('.LinkButton > span:nth-child(1) > div:nth-child(1) > p:nth-child(1)').is_displayed(),
                        "Landing Page not found")

    def test_sign_up(self):
        self.wait_for_element('.LinkButton > span:nth-child(1) > div:nth-child(1) > p:nth-child(1)', By.CSS_SELECTOR).click()
        # cookie banner / is not visible after the click
        # self.wait_for_element('button.button___button___1RG-w:nth-child(1) > span:nth-child(1) > span:nth-child(1)', By.CSS_SELECTOR).click()
        # self.assertFalse(self.driver.find_element_by_css_selector('button.button___button___1RG-w:nth-child(1) > span:nth-child(1) > span:nth-child(1)').is_displayed(),
        #                  "Cookie banner is still visible")
        self.wait_for_element('#firstName--1', By.CSS_SELECTOR).send_keys('Trall')
        self.driver.find_element_by_css_selector('#lastName--2').send_keys('Reff')
        self.driver.find_element_by_css_selector('#emailWithConfirmation-email--4').send_keys('xpdazn+cht001@gmail.com')
        self.driver.find_element_by_css_selector('#emailWithConfirmation-confirmEmail--5').send_keys('xpdazn+cht001@gmail.com')
        self.driver.find_element_by_css_selector('#password--6').send_keys('12345a')
        # self.driver.find_element_by_id('#create-account__button').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('.button___button-text___3KgNu').click()
        self.wait_for_element('.paymentDetails___payment-components-wrapper___gGF1d > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)', By.CSS_SELECTOR).click()
        self.driver.find_element_by_css_selector('#creditCardNumber--8').send_keys('4111111111111111')
        self.driver.find_element_by_css_selector('input.multipleInputsField___input___eDvWS:nth-child(1)').send_keys('102020')
        self.driver.find_element_by_css_selector('#securityCode--10').send_keys('737')
        time.sleep(1)
        self.driver.find_element_by_css_selector('.button___inner-label___3m6pQ > span:nth-child(1)').click()
        self.wait_for_element('.signUpConfirmation___details-title___3MUPf', By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector('.button___button-text___3KgNu').click()
        self.wait_for_element('.header-nav___right-nav___3eW6Q > li:nth-child(1) > button:nth-child(1)', By.CSS_SELECTOR).click()
        time.sleep(1)
        # element to be cliclable from expected conditions
        ############################################

        self.driver.find_elements_by_link_text('Sign Out').click()
        # self.wait_for_element('#MY-DAZN-MENU-LIST-ITEM', By.ID).click()
        self.wait_for_element('button.buttons___button___1NQJe:nth-child(1)', By.CSS_SELECTOR).click()
        self.assertTrue(self.driver.find_element_by_id('#email--1').is_displayed(),
                        "Sign in page is not displayed")

    def test_sign_out(self):
        self.wait_for_element('.linkButton > p:nth-child(1) > a:nth-child(2)', By.CSS_SELECTOR).click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('#email--1').send_keys('xpdazn+cht001@gmail.com')
        self.driver.find_element_by_css_selector('#password--2').send_keys('12345a')
        time.sleep(1)
        self.driver.find_element_by_css_selector('button.button___button___1RG-w:nth-child(2) > span:nth-child(1)').click()
        self.wait_for_element('.header-nav___right-nav___3eW6Q > li:nth-child(1) > button:nth-child(1)', By.CSS_SELECTOR).click()
        time.sleep(1)

        #############################################

        self.driver.find_elements_by_link_text('Sign Out').click()
        # self.wait_for_element('#MY-DAZN-MENU-LIST-ITEM', By.ID).click()
        self.wait_for_element('button.buttons___button___1NQJe:nth-child(1)', By.CSS_SELECTOR).click()
        self.assertTrue(self.driver.find_element_by_id('#email--1').is_displayed(),
                        "Sign in page is not displayed")
