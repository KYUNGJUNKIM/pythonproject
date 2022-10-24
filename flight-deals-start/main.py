from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/9f2b158f2343441358928ec46be85fed/flightManager/prices"
flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

data_manager.update_customer()

for i in range(len(sheet_data)):
    if sheet_data[i]["iataCode"] == "":
        row = sheet_data[i]
        row["iataCode"] = flight_search.get_destination_code(row["city"])

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=180)

for destination in sheet_data:
    flight = flight_search.check_flights(
        "SEL",
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        print(f"Price Alert: Lower Price Ticket bound for {destination['city']} exists.")
        headers = {"Authorization": "Basic a3l1bmdqdW46MTIzNA=="}
        destination["lowestPrice"] = flight.price
        new_data = {
            "price": {
                "lowestPrice": destination["lowestPrice"]
            }
        }
        response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{destination['id']}",
                                json=new_data,
                                headers=headers)
        # smtp = smtplib.SMTP("jun9894@gmail.com")
        # smtp.starttls()
        # smtp.login("jun9894@snu.ac.kr", "1234")
        # smtp.sendmail(from_addr="jun9894@snu.ac.kr",
        #               to_addrs="jun9894@gmail.com",
        #               msg="Subject:Price Down\n\n Check Our Website to get flight ticket with lowest price"
        #               )

        if flight.stop_overs > 0:
            print(f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}.")

