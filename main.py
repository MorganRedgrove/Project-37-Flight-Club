#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time
import data_manager
import flight_search
import flight_data
import notification_manager


dm = data_manager.DataManager()
sheet_data = dm.get_data()

fs = flight_search.FlightSearch()

fd = flight_data.FlightData()

nm = notification_manager.NotificationManager()

for dict in sheet_data["prices"]:
    if dict["iataCode"] == "":
        dict["iataCode"] = fs.get_iata(city=dict["city"])
    flight_data = fs.get_flights(iata=dict["iataCode"])
    try:
        price = fd.get_price(flight_data)
    except ValueError:
        continue
    else:
        if price < dict["lowestPrice"]:
            dict = fd.get_dict(flight_data,price)
            loc_1 = dict["cityFrom"]
            loc_2 = dict["cityTo"]
            iata_1 = dict["flyFrom"]
            iata_2 = dict["flyTo"]
            dpt = time.strftime("%d/%m/%Y", time.localtime(dict["route"][0]["dTime"]))
            rtn = time.strftime("%d/%m/%Y", time.localtime(dict["route"][1]["dTime"]))
            body = f"There is a cheap flight for £{price} from {loc_1}-{iata_1} to {loc_2}-{iata_2}, from {dpt} to {rtn}"
            # nm.send_sms(body)
            print(body)

# n_row = len(sheet_data["prices"])
# for num in range(0,n_row):
#     data.ROW = num+2
#     data.edit_data(city=sheet_data["prices"][num]["city"], iata=sheet_data["prices"][num]["iataCode"], l_price=sheet_data["prices"][num]["lowestPrice"])
#
