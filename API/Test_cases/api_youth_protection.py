import unittest
from API.Lib.token import mislToken
from API.Lib.lib import Lib
# import time

class ApiTests(unittest.TestCase):
    base_url = 'https://eiywmn8jah.execute-api.eu-central-1.amazonaws.com/stage'
    headers = {'Authorization': f"Bearer {mislToken['STAGE']}",
               'Accept': 'application/json',
               'content-type': 'application/json'}
    lib = None

    def setUp(self):
        self.lib = Lib()
        test_name = unittest.TestCase.id(self)
        print("\n", test_name)

    # def tearDown(self):
    #     time.sleep(1)

    def test_01_put_id(self):
        self.lib.put_id(self.base_url, self.headers, "1165515725980514928031808", "PASSPORT")

    def test_02_get_id(self):
        self.lib.get_id(self.base_url, self.headers)

    def test_03_put_pin(self):
        self.lib.put_pin(self.base_url, self.headers, "1234")

    def test_04_get_id(self):
        self.lib.get_id(self.base_url, self.headers)

    def test_05_post_pin(self):
        self.lib.post_pin(self.base_url, self.headers, "1234")

    def test_06_post_pin(self):
        self.lib.post_pin(self.base_url, self.headers, "1233")
