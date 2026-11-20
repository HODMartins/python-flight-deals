

class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(
        self,
        price="N/A",
        origin_airport="N/A",
        destination_airport="N/A",
        from_date="N/A",
        to_date="N/A"
    ):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.from_date = from_date
        self.to_date = to_date

    def find_cheapest_flight(self, all_flights):

        valid_flights = [item for item in all_flights if item.get("price") is not None]

        if not valid_flights:
            return FlightData()
        try:
            cheapest_flight = min(valid_flights, key=lambda item: item["price"])

            self.price = cheapest_flight["price"]
            self.origin_airport = cheapest_flight["flights"][0]["departure_airport"]["id"]
            self.destination_airport = cheapest_flight["flights"][-1]["arrival_airport"]["id"]
            self.from_date = cheapest_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]

            return FlightData(
                price =  int(self.price),
                origin_airport = self.origin_airport,
                destination_airport = self.destination_airport,
                from_date = self.from_date
            )
        except (KeyError, IndexError, TypeError, AttributeError) as error:
            print(f"Error finding cheapest flight: {error}")
            return FlightData()
        

