import unittest
from API.Lib.token import mislToken
from API.Lib.lib import Lib
# import time

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
        self.lib.get_devices(self.base_url, self.headers)

    # register a device
    def test_02_post_devices(self):
        self.lib.post_devices(self.base_url, self.headers, "da3ec4c2-bd81-11e7-abc4-cec278b6b50a")

    # check if the device was registered properly
    def test_03_get_devices(self):
        self.lib.get_devices(self.base_url, self.headers)

    # delete registered devices from provided deviceUUID
    def test_04__delete_devices(self):
        self.lib.delete_selected_device(self.base_url, self.headers, "da3ec4c2-bd81-11e7-abc4-cec278b6b50a")

    # get the list of favourite competitors
    def test_05_get_favourites(self):
        self.lib.get_all_favourites(self.base_url, self.headers)

    # delete selected competitor
    def test_06_delete_reminders(self):
        self.lib.delete_selected_reminders(self.base_url, self.headers, "competitor", "ba25ib8pofxr85hkbs8lt7kw7")

    # get the list of favourite competitors - should be empty
    def test_07_get_favourites(self):
        self.lib.get_all_favourites(self.base_url, self.headers)

    # get the list of reminders
    def test_08_get_reminders(self):
        self.lib.get_reminders(self.base_url, self.headers)

    # delete selected event reminder
    def test_09_delete_reminders(self):
        self.lib.delete_reminders_provided_by_id(self.base_url, self.headers, "ba25ib8pofxr85hkbs8lt7kw7,"
                                                                   "er5n2uejchvb5ynd8r1x6w38q,"
                                                                   "6by3h89i2eykc341oz7lv1ddd,"
                                                                   "7ad69ngbpjuyzv96drf8d9sn2,"
                                                                   "82livqv96ktbj7ub3pz9y2sfe,"
                                                                   "26big9spmo6m1d0r8a7xtk9e0")

    # get the list of reminders - should be empty
    def test_10_get_reminders(self):
        self.lib.get_reminders(self.base_url, self.headers)

    # post reminder for event, competition or competitor - in this case event
    def test_11_post_reminders(self):
        self.lib.post_reminders(self.base_url, self.headers, "competitor", "ba25ib8pofxr85hkbs8lt7kw7") # Poland
        self.lib.post_reminders(self.base_url, self.headers, "event", "er5n2uejchvb5ynd8r1x6w38q") # Lakers @ Nuggets
        self.lib.post_reminders(self.base_url, self.headers, "competition", "6by3h89i2eykc341oz7lv1ddd") # Bundesliga
        self.lib.post_reminders(self.base_url, self.headers, "competitor", "7ad69ngbpjuyzv96drf8d9sn2") # Leverkusen
        self.lib.post_reminders(self.base_url, self.headers, "event", "82livqv96ktbj7ub3pz9y2sfe") # Patriots @ Texans
        self.lib.post_reminders(self.base_url, self.headers, "event", "5o5u929p8enn3pv3u9x7uiugf") # Dart highlights


    # get the list of reminders, event or competition
    def test_12_get_reminders(self):
        self.lib.get_reminders(self.base_url, self.headers)

    # post reminder for event, competition or competitor - in this case competitor
    def test_13_post_reminders(self):
        self.lib.post_reminders(self.base_url, self.headers, "event", "5o5u929p8enn3pv3u9x7uiugf") # Dart highlights
        self.lib.post_reminders(self.base_url, self.headers, "event", "26big9spmo6m1d0r8a7xtk9e0") # Biathlon
        self.lib.post_reminders(self.base_url, self.headers, "event", "lf3blyicw3c6pb1myuj05h08")  # Biathlon
        self.lib.post_reminders(self.base_url, self.headers, "event", "72x75q34929tsqj3rvyfwxpsx")  # Biathlon
        self.lib.post_reminders(self.base_url, self.headers, "event", "88f8dudtpqk8hk4cyghcejwsq") # Pool
        self.lib.post_reminders(self.base_url, self.headers, "competition", "wy3kluvb4efae1of0d8146c1")  # Pool

    # get the list of favourites - previously posted competitor
    def test_14_get_favourites(self):
        self.lib.get_all_favourites(self.base_url, self.headers)

    def test_15_get_events_by_id(self):
        self.lib.get_all_fav_by_event_id(self.base_url, self.headers, "88f8dudtpqk8hk4cyghcejwsq")

    def test_16_get_reminders(self):
        self.lib.get_reminders(self.base_url, self.headers)

    def test_17_get_favourites_by_id(self):
        self.lib.get_selected_favourites(self.base_url, self.headers, "72x75q34929tsqj3rvyfwxpsx")

    def test_18_put_reminders(self):
        self.lib.put_reminders(self.base_url, self.headers, "competition", "wy3kluvb4efae1of0d8146c1")

    def test_19_get_events_by_fav(self):
        self.lib.get_all_fav_by_event_id(self.base_url, self.headers, "er5n2uejchvb5ynd8r1x6w38q")