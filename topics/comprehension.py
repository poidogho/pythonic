import re

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# naive approach
for numIdx in range(0, len(numbers)):
    squaredNum = numbers[numIdx] * numbers[numIdx]
    numbers[numIdx] = squaredNum

print(numbers)
# pep 20 approach using list comprehension
numbers = [num ** 2 for num in numbers]
print(numbers)

# get first 20 even nums
even_nums = [x * 2 for x in range(20)]
print('*****first 20 even nums')
print(even_nums)

# convert fruits to upper case letters
fruits = ['watermelon', 'apple', 'mango', 'KIWI',
          'apricot', 'guava']
upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)

'''
Dictionary comprehension
'''
animals = ['OWL', 'bADGER', 'LION', 'tiger', 'wolf']
dict_animals = {animal.lower(): len(animal) for animal in animals}
print(dict_animals)
'''
{'owl': 3, 'badger': 6, 'lion': 4, 'tiger': 5, 'wolf': 4}
'''

'''
sort comprehension
'''
with open('./mary.txt') as mary_in:
    s = {w.lower() for ln in mary_in for w in re.split(r'\W+', ln) if w}

print(s)
