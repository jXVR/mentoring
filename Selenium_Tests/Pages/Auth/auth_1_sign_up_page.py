from selenium.webdriver.common.by import By
from Selenium_Tests.Lib.lib import Lib


class SignUpPageMassive:
    url = "https://stag.dazn.com/en-JP/account/signup"

    def __init__(self, driver):
        self.driver = driver
        self.lib = Lib(driver)

    create_account_button_css = ".signup"
    active_create_account_button_css = "/html/body/div[2]/div/div[1]/div[1]/div/form/fieldset/div[5]/button"

    first_name_css = "#signUpFirstName"
    last_name_css = "#signUpLastName"
    email_css = "#signUpEmail"
    password_css = "#signUpPassword"
    repeat_password_css = "#signUpPasswordRepeat"
    marketing_opt_css = ".Checkbox"

    def fill_first_name_field(self, text):
        first_name_field = self.driver.find_element_by_css_selector(self.first_name_css)
        first_name_field.clear()
        first_name_field.send_keys(text)

    def fill_last_name_field(self, text):
        last_name = self.driver.find_element_by_css_selector(self.last_name_css)
        last_name.clear()
        last_name.send_keys(text)

    def fill_email_field(self, text):
        email_field = self.driver.find_element_by_css_selector(self.email_css)
        email_field.clear()
        email_field.send_keys(text)

    def fill_password_field(self, text):
        password_field = self.driver.find_element_by_css_selector(self.password_css)
        password_field.clear()
        password_field.send_keys(text)

    def fill_repeat_password_field(self, text):
        password_field = self.driver.find_element_by_css_selector(self.repeat_password_css)
        password_field.clear()
        password_field.send_keys(text)

    def click_marketing_opt(self):
        marketing_opt = self.driver.find_element_by_css_selector(self.marketing_opt_css)
        marketing_opt.click()

    def click_sign_up_button(self):
        sign_up_button = self.driver.find_element_by_css_selector(self.active_create_account_button_css)
        sign_up_button.click()

    def wait_for_page_to_be_open(self):
        self.lib.wait_for_element(self.create_account_button_css, By.CSS_SELECTOR)


    def fill_sign_up_user_details(self, fname, lname, email, password, repeat_password):
        self.wait_for_page_to_be_open()
        self.fill_first_name_field(fname)
        self.fill_last_name_field(lname)
        self.fill_email_field(email)
        self.fill_password_field(password)
        self.fill_repeat_password_field(repeat_password)
        self.click_marketing_opt()
        # time.sleep(2)
        # self.click_sign_up_button()


