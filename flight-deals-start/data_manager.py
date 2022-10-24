import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/9f2b158f2343441358928ec46be85fed/flightManager/prices"
CUSTOMER_ENDPOINT = "https://api.sheety.co/9f2b158f2343441358928ec46be85fed/flightManager/customers"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        headers = {"Authorization": "Basic a3l1bmdqdW46MTIzNA=="}
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        headers = {"Authorization": "Basic a3l1bmdqdW46MTIzNA=="}
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=headers
            )
            print(response.text)

    def update_customer(self):
        headers = {"Authorization": "Basic a3l1bmdqdW46MTIzNA=="}
        first = input("Enter Your First Name: ")
        last = input("Enter Your Last Name: ")
        email = input("Enter Your Email: ")

        new_data = {
            "customer": {
                "firstName": first,
                "lastName": last,
                "email": email
            }
        }

        response = requests.post(url=CUSTOMER_ENDPOINT, headers=headers, json=new_data)
        return response.text

