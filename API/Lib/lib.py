import requests
import json

class Lib:

    # Helpers, console prints
    def return_response(self, response):
        body = response.json()
        code = response.status_code
        response_headers = response.headers
        content_type_header = response_headers['Content-Type']
        time = response.elapsed.microseconds
        print(body, code, content_type_header, time)

    def return_response_delete(self, response):
        code = response.status_code
        response_headers = response.headers
        content_type_header = response_headers['Content-Type']
        time = response.elapsed.microseconds
        print("Code:", code, "Content Type:", content_type_header, "Time:", time)

    # API calls - favourites
    def get_devices(self, base_url, headers):
        url = f'{base_url}/devices'
        response = requests.get(url, headers=headers)
        self.return_response(response)

    def post_devices(self, base_url, headers, deviceUUID):
        url = f'{base_url}/devices'
        data = json.dumps({"deviceUUID": f"{deviceUUID}",
                           "fcmToken": "0d63b512573dce7be5eb53bab58a5625",
                           "apnToken": "740f4707-bebcf74f-9b7c25d4-8e335894-5f6aa01d-a5ddb387-462c7eaf-61bb78ad",
                           "platform": "Android",
                           "languageCode": "en",
                           "countryCode": "de"})
        response = requests.post(url, data, headers=headers)
        self.return_response(response)

    def delete_selected_device(self, base_url, headers, deviceUUID):
        url = f'{base_url}/devices/{deviceUUID}'
        response = requests.delete(url, headers=headers)
        self.return_response_delete(response)

    def get_all_favourites(self, base_url, headers):
        url = f'{base_url}/favourites'
        params = {"languageCode": "en",
                  "countryCode": "de",
                  "extended": False}
        response = requests.get(url, params, headers=headers)
        self.return_response(response)
        with open('../Json/favourites.json', 'w') as favourites_file:
            json.dump(response.json(), favourites_file)

    def get_selected_favourites(self, base_url, headers, id):
        url = f'{base_url}/favourites/{id}'
        params = {"languageCode": "en",
                  "countryCode": "de",
                  "extended": False}
        response = requests.get(url, params, headers=headers)
        self.return_response(response)
        with open('../Json/favourites_tied_to_id.json', 'w') as favourites_file:
            json.dump(response.json(), favourites_file)

    def get_reminders(self, base_url, headers):
        url = f'{base_url}/reminders'
        params = {"languageCode": "en",
                  "countryCode": "de",}
        response = requests.get(url, params, headers=headers)
        self.return_response(response)
        with open('../Json/reminders.json', 'w') as favourites_file:
            json.dump(response.json(), favourites_file)

    def delete_reminders_provided_by_id(self, base_url, headers, eventIds):
        url = f'{base_url}/reminders/{eventIds}'
        response = requests.delete(url, headers=headers)
        self.return_response_delete(response)

    def post_reminders(self, base_url, headers, event_type, favouriteId):
        url = f'{base_url}/reminders/{event_type}'
        data = json.dumps({"favouriteId": f"{favouriteId}",
                           "languageCode": "en",
                           "countryCode": "de"})
        response = requests.post(url, data, headers=headers)
        self.return_response(response)

    def put_reminders(self, base_url, headers, event_type, favouriteId):
        url = f'{base_url}/reminders/{event_type}/{favouriteId}'
        print(url)
        data = json.dumps({"push": True,
                           "rail": True})
        response = requests.put(url, data, headers=headers)
        self.return_response(response)

    def delete_selected_reminders(self, base_url, headers, event_type, favouriteId):
        url = f'{base_url}/reminders/{event_type}/{favouriteId}'
        response = requests.delete(url, headers=headers)
        self.return_response_delete(response)

    def get_all_fav_by_event_id(self, base_url, headers, favouriteId):
        url = f'{base_url}/events/{favouriteId}/favourites'
        params = {"languageCode": "en",
                  "countryCode": "de",}
        response = requests.get(url, params, headers=headers)
        self.return_response(response)
        with open('../Json/event_by_id.json', 'w') as favourites_file:
            json.dump(response.json(), favourites_file)

    # API calls - youth protection

    def put_id(self, base_url, headers, id, type):
        url = f"{base_url}/id"
        data = json.dumps({'id': f'{id}',
                           'type': f'{type}'})
        response = requests.put(url, data, headers=headers)
        self.return_response(response)

    def get_id(self, base_url, headers):
        url = f"{base_url}/id"
        response = requests.get(url, headers=headers)
        self.return_response(response)

    def put_pin(self, base_url, headers, pin):
        url = f"{base_url}/pin"
        data =  json.dumps({"pin": f"{pin}"})
        response = requests.put(url, data, headers=headers)
        self.return_response(response)

    def post_pin(self, base_url, headers, pin):
        url = f"{base_url}/pin"
        data =  json.dumps({"pin": f"{pin}"})
        response = requests.post(url, data, headers=headers)
        self.return_response(response)
