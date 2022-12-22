numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# naive approach
for numIdx in range(0, len(numbers)):
    squaredNum = numbers[numIdx] * numbers[numIdx]
    numbers[numIdx] = squaredNum

print(numbers)
# pep 20 approach using list comprehension
numbers = [num ** 2 for num in numbers]
print(numbers)
