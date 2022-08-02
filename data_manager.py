import requests
from pprint import pprint

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.API_BACKEND = "https://api.sheety.co/f4733177fc58fcf300746c50f4f34d9f/flightDeals/prices"
        self.TOKEN = ""
        self.JSON = {
            "price": {
                "city": "",
                "iataCode": "",
                "lowestPrice": "",
            }

        }
        self.HEADERS = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {self.TOKEN}"
        }
        self.flight_data = {

        }
        self.ROW=0

    def add_data(self,city,iata,l_price):
        self.JSON["price"]["city"] = city
        self.JSON["price"]["iataCode"] = iata
        self.JSON["price"]["lowestPrice"] = l_price
        self.response = requests.post(url=self.API_BACKEND, headers=self.HEADERS, json=self.JSON)
        self.response.raise_for_status()

    def edit_data(self,city,iata,l_price):
        self.JSON["price"]["city"] = city
        self.JSON["price"]["iataCode"] = iata
        self.JSON["price"]["lowestPrice"] = l_price
        self.response = requests.put(url=f"{self.API_BACKEND}/{self.ROW}", headers=self.HEADERS, json=self.JSON)
        self.response.raise_for_status()

    def get_data(self):
        self.response = requests.get(url=self.API_BACKEND, headers=self.HEADERS)
        self.response.raise_for_status()
        self.DATA = self.response.json()
        return self.DATA



