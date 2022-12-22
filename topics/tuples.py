# tuples are used to group related items together

person = ('odafe', 'idogho', 36)
print(person)

# tuples can do without the parenthesis
person = 'odafe', 'idogho', 32
print(person, type(person))

# tuples can be a single item but it must end with a comma
person = 'odafe',
print(person, type(person))

# tuples with a single item without a comma at the end could result in issues
person = 'odafe'
print(person, type(person))
# the above is a string

# unpacking tuples
# rather than use index to get values in tuples, unpack the values

person = ('odafe', 'idogho', 36)
# dont just do this
print('dont use index')
print(person[0], person[1], person[2])

# do this instead
first_name, last_name, age = person
print(first_name, last_name, age)

# better example
people = [
    ('odafe', 'idogho', 36),
    ('odafe2', 'idogho2', 362),
    ('odafe3', 'idogho3', 363),
    ('odafe4', 'idogho4', 364),
    ('odafe5', 'idogho5', 365),
]

print('loop values')

for first_name, last_name, age in people:
    print('{} {} {}'.format(first_name, last_name, age))

print('=====================')
# you can also do this
for person in people:
    print(*person)
