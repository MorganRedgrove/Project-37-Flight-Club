class FlightData:
    #This class is responsible for structuring the flight data.
    def get_price(self,data):
        self.PRICE_LIST=[]
        for dict in data["data"]:
            self.PRICE_LIST.append(dict["price"])
        return min(self.PRICE_LIST)

    def get_dict(self,data,price):
        for dict in data["data"]:
            if dict["price"] == price:
                return dict



