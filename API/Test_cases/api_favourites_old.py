import json
import unittest
import requests
from API.Lib.lib import Lib
from API.Lib.token import mislToken


class ApiTests(unittest.TestCase):
    base_url = 'https://0g0ams9m2b.execute-api.eu-central-1.amazonaws.com/stage/eu/v1/notifications'
    headers = {'Authorization': f"Bearer {mislToken['STAGE']}",
               'Accept': 'application/json',
               'content-type': 'application/json'}
    lib = None

    def setUp(self):
        self.lib = Lib()
        test_name = unittest.TestCase.id(self)
        print("\n", test_name)

    # def tearDown(self):
    # time.sleep(1)

    # get the list of all registered devices
    def test_01_get_devices(self):
        url = f'{self.base_url}/devices'
        response = requests.get(url, headers=self.headers)
        self.lib.return_response(response)

    # register a device
    def test_02_post_devices(self):
        url = f'{self.base_url}/devices'
        data = json.dumps({"deviceUUID": "da3ec4c2-bd81-11e7-abc4-cec278b6b50a",
                           "fcmToken": "0d63b512573dce7be5eb53bab58a5625",
                           "apnToken": "740f4707-bebcf74f-9b7c25d4-8e335894-5f6aa01d-a5ddb387-462c7eaf-61bb78ad",
                           "platform": "Android",
                           "languageCode": "en",
                           "countryCode": "de"})
        response = requests.post(url, data, headers=self.headers)
        self.lib.return_response(response)

    # check if the device was registered properly
    def test_03_get_devices(self):
        url = f'{self.base_url}/devices'
        response = requests.get(url, headers=self.headers)
        self.lib.return_response(response)

    # delete registered devices from provided deviceUUID
    def test_04__delete_devices(self):
        deviceUUID = "da3ec4c2-bd81-11e7-abc4-cec278b6b50a"
        url = f'{self.base_url}/devices/{deviceUUID}'
        response = requests.delete(url, headers=self.headers)
        self.lib.return_response_delete(response)

    # get the list of favourite competitors
    def test_05_get_favourites(self):
        self.lib.get_favourites(self.base_url, self.headers)
        # self.lib.return_response(response)

    # delete selected competitor
    def test_06_delete_reminders(self):
        reminders_type = "competitor"
        params = {"eventIds": "ba25ib8pofxr85hkbs8lt7kw7"}
        url = f'{self.base_url}/reminders/{reminders_type}/{params["eventIds"]}'
        response = requests.delete(url, headers=self.headers)
        self.lib.return_response_delete(response)

    # get the list of favourite competitors - should be empty
    def test_07_get_favourites(self):
        url = f'{self.base_url}/favourites'
        params = {"languageCode": "en",
                  "countryCode": "de",
                  "extended": False}
        response = requests.get(url, params, headers=self.headers)
        self.lib.return_response(response)

    # get the list of reminders
    def test_08_get_reminders(self):
        url = f'{self.base_url}/reminders'
        params = {"languageCode": "en",
                  "countryCode": "de", }
        response = requests.get(url, params, headers=self.headers)
        self.lib.return_response(response)

    # delete selected event reminder
    def test_09_delete_reminders(self):
        reminders_type = "event"
        params = {"eventIds": "4rbcdpopje9cclllzs1w86zqi"}
        url = f'{self.base_url}/reminders/{params["eventIds"]}'
        response = requests.delete(url, headers=self.headers)
        self.lib.return_response_delete(response)

    # get the list of reminders - should be empty
    def test_10_get_reminders(self):
        url = f'{self.base_url}/reminders'
        params = {"languageCode": "en",
                  "countryCode": "de", }
        response = requests.get(url, params, headers=self.headers)
        self.lib.return_response(response)

    # post reminder for event, competition or competitor - in this case event
    def test_11_post_reminders(self):
        reminders_type = "event"
        url = f'{self.base_url}/reminders/{reminders_type}'
        data = json.dumps({"favouriteId": "4rbcdpopje9cclllzs1w86zqi",
                           "languageCode": "en",
                           "countryCode": "de"})
        response = requests.post(url, data, headers=self.headers)
        self.lib.return_response(response)

    # get the list of reminders, event or competition
    def test_12_get_reminders(self):
        url = f'{self.base_url}/reminders'
        params = {"languageCode": "en",
                  "countryCode": "de", }
        response = requests.get(url, params, headers=self.headers)
        self.lib.return_response(response)

    # post competition

    # post reminder for event, competition or competitor - in this case competitor
    def test_13_post_reminders(self):
        reminders_type = "competitor"
        url = f'{self.base_url}/reminders/{reminders_type}'
        data = json.dumps({"favouriteId": "ba25ib8pofxr85hkbs8lt7kw7",
                           "languageCode": "en",
                           "countryCode": "de"})
        response = requests.post(url, data, headers=self.headers)
        self.lib.return_response(response)

    # get the list of favourites - previously posted competitor
    def test_14_get_favourites(self):
        url = f'{self.base_url}/favourites'
        params = {"languageCode": "en",
                  "countryCode": "de",
                  "extended": False}
        response = requests.get(url, params, headers=self.headers)
        self.lib.return_response(response)

    def test_15_get_favourites_by_id(self):
        event_id = "ba25ib8pofxr85hkbs8lt7kw7"
        url = f'{self.base_url}/favourites/{event_id}'
        params = {"languageCode": "en",
                  "countryCode": "de",
                  "extended": False}
        response = requests.get(url, params, headers=self.headers)
        self.lib.return_response(response)

    def test_16_get_reminders(self):
        url = f'{self.base_url}/reminders'
        params = {"languageCode": "en",
                  "countryCode": "de", }
        response = requests.get(url, params, headers=self.headers)
        self.lib.return_response(response)
