import requests
import datetime as dt

tommorow = (dt.datetime.today() + dt.timedelta(days=1))
date = tommorow.strftime("%d/%m/%Y")
date_180 = (tommorow + dt.timedelta(days=180)).strftime("%d/%m/%Y")


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.API_BACKEND = "https://tequila-api.kiwi.com"
        self.HEADERS = {
            "accept": "application/json",
            "apikey": "",
        }
        self.JSON = {
            #get_iata
            "term": "",
            #get_price
            "fly_from": "LHR",
            "fly_to": "",
            "date_from": date,
            "date_to": date_180,
            "flight_type": "round",
            "curr": "GBP",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": 0,
        }


    def get_iata(self, city):
        self.JSON["term"] = city
        self.FUNC = "/locations/query"
        self.response = requests.get(url=f"{self.API_BACKEND}{self.FUNC}", headers=self.HEADERS, params=self.JSON)
        self.response.raise_for_status()
        self.DATA = self.response.json()
        return self.DATA["locations"][0]["code"]

    def get_flights(self, iata):
        self.JSON["fly_to"] = iata
        self.FUNC = "/search"
        self.response = requests.get(url=f"{self.API_BACKEND}{self.FUNC}", headers=self.HEADERS, params=self.JSON)
        self.response.raise_for_status()
        self.DATA = self.response.json()
        return self.DATA
