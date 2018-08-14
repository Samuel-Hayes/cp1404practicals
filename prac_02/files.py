name = str(input("Please enter your name: "))
out_file = open('name.txt', 'w')
print(name, file=out_file)
out_file.close()

in_file = open('name.txt', 'r')
read_name = in_file.readline()
print("Your name is {}".format(read_name))
in_file.close()

number_file = open('numbers.txt', 'r')
total = 0
for line in number_file:
    number = int(line)
    total += number
print(total)
number_file.close()
