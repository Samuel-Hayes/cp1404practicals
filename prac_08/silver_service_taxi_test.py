from prac_08.silver_service_taxi import SilverServiceTaxi

SSTaxi = SilverServiceTaxi("Hummer", 200, 4)
print(SSTaxi)

Hummer = SilverServiceTaxi("Hummer2", 200, 2)
Hummer.drive(18)
print(Hummer.get_fare())
