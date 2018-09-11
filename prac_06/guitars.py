from prac_06.guitar import Guitar
guitars = []
# name = input("Guitar name is: ")

# while name != "":
#     age = int(input("Age for {}: ".format(name)))
#     value = int(input("Value for {}: ".format(name)))
#     guitars.append(Guitar(name, age, value))
#     name = input("Guitar name is: ")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
print("These are my guitars:")
for i, guitar in enumerate(guitars):
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f}".format(i + 1, guitar.name, guitar.year, guitar.cost))
print(guitars)
print(Guitar)
