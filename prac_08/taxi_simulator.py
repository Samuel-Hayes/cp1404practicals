from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
current_taxi = None
print("Lets drive:\n q)uit, c)hoose taxi, d)rive")
choice = input('>>>')
while choice != 'q'.upper():
    if choice == 'c'.upper():
        print("Taxis available:")
        i = 0
        for taxi in taxis:
            print(i + print(taxis[i]))
            i += 1
        current_taxi = input("Choose taxi: ")
    elif choice == 'd'.upper():
        distance = int(input("Distance: "))
        current_taxi.drive(distance)
        total_fare += current_taxi.get_fare()
    else:
        print("Please enter valid input")
    choice = input('>>>')
print("Your total taxi fare is: ${}".format(total_fare))
