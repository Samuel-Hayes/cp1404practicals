from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
current_taxi = None
total_fare = 0
print("Lets drive:\n q)uit, c)hoose taxi, d)rive")
choice = str(input('>>>')).upper()


def show_taxis():
    i = 0
    for taxi in taxis:
        print("{}. {}".format(i, (taxis[i])))
        i += 1


while choice != 'Q':
    if choice == 'C':
        print("Taxis available:")
        show_taxis()
        taxi_choice = int(input("Choose taxi: "))
        current_taxi = taxis[taxi_choice]
        print("Your taxi is: {}".format(current_taxi))
    elif choice == 'D':
        distance = int(input("Distance: "))
        current_taxi.drive(distance)
        print("Your {} trip will cost you {}".format(current_taxi.name, current_taxi.get_fare()))
        total_fare += current_taxi.get_fare()
        print("Bill to date: ${}".format(total_fare))
    else:
        print("Please enter valid input")
    print("q)uit, c)hoose taxi, d)rive")
    choice = str(input('>>>')).upper()
show_taxis()
print("Your total taxi fare is: ${}".format(total_fare))
