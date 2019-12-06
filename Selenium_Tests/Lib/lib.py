from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
from seleniumwire import webdriver
import pandas as pd


class Lib:
    def __init__(self, driver):
        self.driver = driver


    def wait_for_element(self, selector, by):
        return WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((by, selector)))
        # return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))


    def get_correlation_id(self):
        for request in self.driver.requests:
            if request.path == "https://stag-eu.dazn.com/misl/eu/v6/Subscribe" and request.method == "POST":
                correlation_id = request.response.headers["x-correlation-id"]
                # print(correlation_id)
                return correlation_id

    def dataframes_to_excel_to_separate_sheets(self, df_list, sheet_list, name):
        writer = pd.ExcelWriter(f"../Output_files/{name}.xlsx", engine='xlsxwriter')
        for df, sheet in zip(df_list, sheet_list):
            df.to_excel(writer, sheet_name=sheet, header=["Age", "Height", "Foot", "Nationality", "Photo URL"],
                      index_label="Name")
        writer.save()

    def dataframe_to_excel_psd2(self, dataframe, name):
        dataframe.to_excel(f"../Output_files/{name}.xlsx", sheet_name=f"{name}",
                           header= ["Emial", "CC Number", "CC Type", "Correlation id"],
                      index_label= "Number" )

def select_driver(browser):
    if browser == "Chrome":
        return webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', seleniumwire_options={'verify_ssl': False})
        # return webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

    elif browser == "Firefox":
        return webdriver.Firefox()
    else:
        return webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
