import requests

class FlightData:

    def __init__(self):
        self.flight_search_amount = 0
        self.sheety_get_endpoint = "https://api.sheety.co/eec27fdcbfd9a3eb7c5570d0b46911a6/flightDealsInputData/prices"



    def pull_search_items(self):
        sheety_get_response = requests.get(url=self.sheety_get_endpoint)
        sheety_get_response.raise_for_status()
        print(f"sheety response data: {sheety_get_response.text}")

        for i in range(0,self.flight_search_amount):
            pass


flight_data = FlightData()
flight_data.pull_search_items()