# This file will need to use the
# DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
import smtplib

gmail_email1 = "jamjam.perey2@gmail.com"  # your personal email that will be sending emails
password = "xdwlvptiiyfhljfa" # changed for security - code will not work due to this
yahoo_app_pw = ""
gmail_email2 = "jamjam.perey@gmail.com"
gmail_smtp = "smtp.gmail.com"

data_manager = DataManager()
data_frm_wksht = data_manager.pull_search_items()

flight_search = FlightSearch(data_frm_wksht)
flight_search.print_google_data()

user_location = input("Please input current location(via IATA Code): ").upper()
user_date_frm = input("Please input beginning vacation date in DD/MM/YYYY: ")
user_date_to = input("Please input ending vacation date in DD/MM/YYYY: ")

flight_search_data = flight_search.get_data_tequila(user_location, user_date_frm, user_date_to)

flight_data = FlightData(flight_search_data, user_date_frm, user_date_to)
flight_data_eval = flight_data.eval_data()

flight_data_final_list = flight_data.eval_data_2(flight_data_eval)

# email data

for data in flight_data_final_list:

    connection = smtplib.SMTP(gmail_smtp, port=587)
    connection.starttls()
    connection.login(user=gmail_email1, password=password)
    connection.sendmail(from_addr=gmail_email1, to_addrs=gmail_email2, msg=f"Subject: There are flight deals today!"
                                                                         f"!\n\nflight to:{data['arrival city name']}\n"
                                                                         f"from: {data['departure city name']}\n"
                                                                         f"outbound date: {data['outbound date']}\n"
                                                                         f"inbound date: {data['inbound date']}\n"
                                                                         f"price: {data['price']}")




