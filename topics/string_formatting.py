'''
{:d} formats argument as an integer
{:03d} formats as integer, 3 columns wide, 0 padding
{:>25s} same but right justified
{:.3f} formats as a float, with 3 decimal places
'''

# using .format
s = 'Try one of these: {0}.png {0}.jpg {0}.bmp'.format('techhalls')
print(s)
'''
Try one of these: techhalls.png techhalls.jpg techhalls.bmp
'''

color = 'blue'
car = 'benz'
print('{} {}'.format(color, car))
'''
blue benz
'''

fahr = 98.4733558
print('{:.3f} degrees farhenhit'.format(fahr))
'''
98.473 degrees farhenhit
'''

value = 12345
print('{0:d} {0:04x} {0:08o} {0:016b}'.format(value))
'''
value in decimal, hex, oct and binary
12345 3039 00030071 0011000000111001
'''

data = {'A': 10, 'B': 20, 'C': 300}
for letter, number in sorted(data.items()):
    print('{} {:4d}'.format(letter, number))
'''
add paddings
A   10
B   20
C  300
'''


'''
Python introduces f string from v3.6 upwards
This adds the formating to within the place holder
example below
'''
# without f string
x = 24
y = 32.5566
name = 'odafe Idogho'
company = 'techhalls'

print('{} is co-founder of {}'.format(name, company))
'''
odafe Idogho is co-founder of techhalls
'''

# with f string
print('{:.2f} {:.2f}'.format(x, y))
'''
24.00 32.56
'''
