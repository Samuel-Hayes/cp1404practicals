from prac_06.guitar import Guitar
guitars = []
name = input("Guitar name is: ")
# while name != "":
#     guitars.append(name)
#     name = input("Guitar name is: ")
#
# for guitar in guitars:
#     age = input("Age for {}: ".format(guitar))
#     value = input("Value for {}: ".format(guitar))
#     guitars.append(Guitar(name, age, value))

while name != "":
    age = input("Age for {}: ".format(name))
    value = input("Value for {}: ".format(name))
    guitars.append(Guitar(name, age, value))
    name = input("Guitar name is: ")

print(guitars)
print(Guitar)
