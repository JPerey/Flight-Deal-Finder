import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.flight_search_amount = 0
        self.sheety_get_endpoint = "https://api.sheety.co/eec27fdcbfd9a3eb7c5570d0b46911a6/flightDealsInputData/prices"

    def pull_search_items(self):
        sheety_get_response = requests.get(url=self.sheety_get_endpoint)
        sheety_get_response.raise_for_status()
        # print(f"sheety response data: {sheety_get_response.json()['prices']}")
        return sheety_get_response.json()['prices']
