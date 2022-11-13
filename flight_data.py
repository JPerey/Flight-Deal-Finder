import requests


class FlightData:
    # this class is responsible for evaluating flight search data

    def __init__(self, flight_search_data):
        self.flight_search_data = flight_search_data

    def eval_data(self):
        filter1_eval_data = []
        for packet in self.flight_search_data:
            if len(packet["data"]) > 0:
                filter1_eval_data.append(packet)
        self.eval_data_2(filter1_eval_data)

    def eval_data_2(self, filter1_eval_data):
        print(filter1_eval_data[1])
