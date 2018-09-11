from prac_06.guitar import Guitar

print("My guitars!")
guitars = []
name = input("Name: ")

while name != "":
    year = int(input("Year: "))
    value = int(input("Cost $: "))
    guitars.append(Guitar(name, year, value))
    print("{} ({}) : ${} added.".format(name, year, value))
    name = input("Name: ")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
print("These are my guitars:")
for i, guitar in enumerate(guitars):
    if guitar.is_vintage():
        vintage_string = " (vintage)"
    else:
        vintage_string = ""
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                              vintage_string))
# print(guitars)
# print(Guitar)
