import random
ticket = [0, 0, 0, 0, 0, 0]
purchase = int(input("How many quick picks? "))
for i in range(purchase):
    for j in range(0, 6, 1):
        ticket[j] = int(random.randint(1, 45))
    ticket.sort()
    print(" ".join("{:2}".format(purchase) for purchase in ticket))
