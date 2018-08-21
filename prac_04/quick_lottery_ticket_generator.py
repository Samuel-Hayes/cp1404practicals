import random
ticket = [0, 0, 0, 0, 0, 0]
purchase = int(input("How many quick picks? "))
for i in range(purchase):       #loops for amount of tickets
    for j in range(0, 6, 1):    #generates 6 random numbers for a ticket
        ticket[j] = int(random.randint(1, 45))
    ticket.sort()   #orders numbers
    print(" ".join("{:2}".format(purchase) for purchase in ticket)) #prints as string
