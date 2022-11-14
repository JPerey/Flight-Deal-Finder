import requests


class FlightData:
    # this class is responsible for evaluating flight search data

    def __init__(self, flight_search_data, outbound_date, inbound_date):
        self.flight_search_data = flight_search_data
        self.outbound_date = outbound_date
        self.inbound_date = inbound_date

    def eval_data(self):
        filter1_eval_data = []
        for packet in self.flight_search_data:
            if len(packet["data"]) > 0:
                filter1_eval_data.append(packet["data"])
        return filter1_eval_data

    def eval_data_2(self, filter1_eval_data):
        data_to_send_email = []

        for packet2 in filter1_eval_data:
            data_to_add = {"price": packet2[0]["price"], "departure city name": packet2[0]["cityFrom"],
                           "departure iata code": packet2[0]["flyFrom"], "arrival city name": packet2[0]["cityTo"],
                           "arrival iata code": packet2[0]["cityCodeTo"], "outbound date": self.outbound_date,
                           "inbound date": self.inbound_date}

            print(f"ONE PACKET: {data_to_add}")

            data_to_send_email.append(data_to_add)
        return data_to_send_email
