import requests
import os


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self, data_frm_wksht):
        self.tequila_endpoint = "http://api.tequila.kiwi.com/v2/search"
        self.data_frm_wksht = data_frm_wksht

    def print_google_data(self):
        # print(f"data from google sheets, passed in: {self.data_frm_wksht}")
        pass

    def get_data_tequila(self, user_location, user_date_frm, user_date_to):
        search_list = []
        headers = {
            "apikey": os.environ.get("apikey"),
        }

        for flight in self.data_frm_wksht:
            flight_search_params = {
                "fly_from": user_location,
                "fly_to": flight["iataCode"],
                "price_to": flight["lowestPrice"],
                "date_from": user_date_frm,
                "date_to": user_date_to,
                "curr": "USD",
                "partner_market": "us"
            }

            try:
                tequila_search_response = requests.get(url=self.tequila_endpoint, params=flight_search_params,
                                                       headers=headers)
                tequila_search_response.raise_for_status()
                tequila_search_response_json = tequila_search_response.json()
                # print(f"{tequila_search_response.json()}")
                search_list.append(tequila_search_response_json)
                print("------------------------------------------------------------------------------------------------"
                      "---------------------------------ADDED ONE---------ADDED ONE------------------------------------"
                      "-----------------------------------------------------------------------------------------------")

            except requests.exceptions.HTTPError as e:
                print(e)
        return search_list

