# This file will need to use the
# DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from tkinter import *

window = Tk()
window.title("Deals - Flight search app")
window.config(padx=20, pady=20)

data_manager = DataManager()
data_frm_wksht = data_manager.pull_search_items()

flight_search = FlightSearch(data_frm_wksht)
flight_search.print_google_data()

user_location = input("Please input current location(via IATA Code): ").upper()
user_date_frm = input("Please input beginning vacation date in DD/MM/YYYY: ")
user_date_to = input("Please input ending vacation date in DD/MM/YYYY: ")

flight_search.get_data_tequila(user_location, user_date_frm, user_date_to)

window.mainloop()
