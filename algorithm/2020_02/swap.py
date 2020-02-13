
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# a = numbers.index(max(numbers[3:]))
numbers[3], numbers[numbers.index(max(numbers[3:]))] = numbers[numbers.index(max(numbers[3:]))], numbers[3]



print(type(numbers.index(max(numbers[3:]))))
print(numbers.index(max(numbers[3:])))