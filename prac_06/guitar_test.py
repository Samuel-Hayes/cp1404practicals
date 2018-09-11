from prac_06.guitar import Guitar

Gibson = Guitar("Gibson", 1922, 1500)
print(Gibson)
print(Gibson.get_age())
print(Gibson.is_vintage())

print("{} get_age() - Expected {}. Got {}".format(Gibson.name, 96, Gibson.get_age()))
print("{} is_vintage() - Expected {}. Got {}".format(Gibson.name, "True", Gibson.is_vintage()))
