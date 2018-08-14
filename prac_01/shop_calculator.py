
items = int(input("Enter number of items: "))
while items < 0:
    print("Invalid number of items!")
    items = 0

total = 0
for i in range(items):
    price = float(input("Price of item: $"))
    total += price
if total > 100.00:
    total -= 0.1*total

print("Total price for {} items is ${:.2f}".format(items, total))
