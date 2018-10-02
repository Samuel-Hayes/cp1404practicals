from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the price for the taxi trip."""
        return round(super().get_fare() + self.flagfall, 1)

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, plus flagfall ${:.2f}".format(super().__str__(),
                                              self.flagfall)
