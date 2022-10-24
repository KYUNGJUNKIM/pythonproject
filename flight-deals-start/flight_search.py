import requests
from flight_data import FlightData
from datetime import datetime, timedelta

API_KEY = "EKKnnKXE7RvoJ2H5agdLeaJLY7agIY3h"
END_POINT = "https://api.tequila.kiwi.com"


class FlightSearch:

    def get_destination_code(self, city_name):
        headers = {"apikey": API_KEY}
        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=f"{END_POINT}/locations/query", headers=headers, params=query)
        data = response.json()["locations"]
        code = data[0]["code"]
        return code

    def check_flights(self, origin_city_code, dest_city_code, from_time, to_time):
        headers = {"apikey": API_KEY}
        parameters = {
            "fly_from": origin_city_code,
            "fly_to": dest_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "KRW"
        }
        response = requests.get(url=f"{END_POINT}/v2/search", headers=headers, params=parameters)
        try:
            data = response.json()["data"][0]

        except IndexError:
            parameters["max_stopovers"] = 1
            response = requests.get(url=f"{END_POINT}/v2/search", headers=headers, params=parameters)

            try:
                data = response.json()["data"][0]
            except IndexError:
                print("We Cannot Find A Flight What You Search For.")
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                print(f"{flight_data.destination_city}: {flight_data.price}원")

                return flight_data

        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                via_city=data["route"][0],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: {flight_data.price}원")

            return flight_data

# headers = {"apikey": API_KEY}
# parameters = {
#     "fly_from": "SEL",
#     "fly_to": "DPS",
#     "date_from": datetime.now().strftime("%d/%m/%Y"),
#     "date_to": (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y"),
#     "nights_in_dst_from": 7,
#     "nights_in_dst_to": 28,
#     "flight_type": "round",
#     "one_for_city": 1,
#     "max_stopovers": 0,
#     "curr": "KRW"
# }
# response = requests.get(url=f"{END_POINT}/v2/search", headers=headers, params=parameters)
# try:
#     data = response.json()["data"]
#     print(data)
# except IndexError:
#     parameters["max_stopovers"] = 1
#     response = requests.get(url=f"{END_POINT}/v2/search", headers=headers, params=parameters)
#     data = response.json()["data"][0]
#     print(data)
#     flight_data = FlightData(
#         price=data["price"],
#         origin_city=data["route"][0]["cityFrom"],
#         origin_airport=data["route"][0]["flyFrom"],
#         destination_city=data["route"][1]["cityTo"],
#         destination_airport=data["route"][1]["flyTo"],
#         out_date=data["route"][0]["local_departure"].split("T")[0],
#         return_date=data["route"][2]["local_departure"].split("T")[0],
#         stop_overs=1,
#         via_city=data["route"][0]["cityTo"]
#     )
#     print(flight_data)
