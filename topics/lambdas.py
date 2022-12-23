'''
Lambdas useful when the act as callbacks
syntax is 
lambda params: expression
synonymous to 
def function-name(params):
    return expression
'''
def addTwoNums(x, y): return x+y


print(addTwoNums(3, 4))

# as a callback


def printResults(func, x, y): return print(func(x, y))


printResults(addTwoNums, 10, 20)

fruits = ['watermelon', 'Apple', 'Mango', 'KIWI',
          'apricot', 'guava']
# using lambda to created sort with lowercase
sorted_fruits = sorted(fruits, key=lambda fruit: fruit.lower())
print('*******sorted fruits********')
print(sorted_fruits)
