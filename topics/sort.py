import re

fruits = [
    'pomegranate', 'cherry', 'appricot', 'Apple', 'BLUEberry', 'FIG',
    'ORANGE', 'Tamarind', 'peach', 'PW'
]

# USING THE INBUILD SORT FUNCTION
sorted_fruits = sorted(fruits)
print({'sorted_fruits': sorted_fruits})

"""
results is as below
{'sorted_fruits': ['Apple', 'BLUEberry', 'FIG', 'ORANGE', 'PW', 
'Tamarind', 'appricot', 'cherry', 'peach', 'pomegranate']}
"""

"""
Looking at the above, we can see that its not the sort we anticipate
we can add a 2nd param to the sort function
"""


def ignore_case(item):
    return item.lower()


sorted_fruits2 = sorted(fruits, key=ignore_case)

print("******************")
print({'proper_sort': sorted_fruits2})
"""
this will give us a sort irrespective of the case
{'proper_sort': ['Apple', 'appricot', 'BLUEberry', 'cherry', 
'FIG', 'ORANGE', 'peach', 'pomegranate', 'PW', 'Tamarind']}
"""

"""
Another example to sort by first the length of a string 
and then by the item itself
"""


def by_length_then_name(name):
    return (len(name), name.lower())


sorted_fruits3 = sorted(fruits, key=by_length_then_name)
print('*********complex sort********')
print({'complex_sort': sorted_fruits3})
'''
RESULT
{'complex_sort': ['PW', 'FIG', 'Apple', 'peach','cherry',
 'ORANGE', 'appricot', 'Tamarind', 'BLUEberry', 'pomegranate']}
'''

books = [
    'A Study of scarlet',
    'the sign of the Four',
    'The hound of the Baskervilles',
    'The valley of fear',
    'The Adventure of sherlock holmes',
    "The memoirs of sherlock holmes",
    "The Return of sherlock holmes",
    'His last Bow',
    "The Case-book of sherlock holmes",
]

'''
using regex, we will sort by stripping each book of the 
words the, a,an
'''

rx_article = re.compile(r'^(the|a|an)\s+', re.I)


def strip_articles(title):
    stripped_title = rx_article.sub('', title.lower())
    return stripped_title


print("**********sort stripping first word*********")
for book in sorted(books, key=strip_articles):
    print(book)
'''
RESULT
The Adventure of sherlock holmes
The Case-book of sherlock holmes
His last Bow
The hound of the Baskervilles
The memoirs of sherlock holmes
The Return of sherlock holmes
the sign of the Four
A Study of scarlet
The valley of fear
'''
