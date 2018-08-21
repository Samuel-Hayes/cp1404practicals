#numbers[0] gives 3
#numbers[-1] gives 2
#numbers[3] gives 1
#numbers[:-1] gives [3, 1, 4, 1, 5, 9]
#numbers[3:4} gives 1
#5 in numbers gives True
#7 in numbers gives False
#"3" in numbers False
#numbers + [6, 5, 3] gives [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[0] = 10
numbers[-1] = 1
print(numbers)
print(numbers[2:])
print(9 in numbers)
