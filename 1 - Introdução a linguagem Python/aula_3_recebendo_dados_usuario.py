"""
Getting user input in Python

input() -> data received as String.

In Python, string is everything within:
* Single quotation marks
* Double quotation marks
* Triple single quotation marks
* Triple double quotation marks

e.g.:
Single quotation marks > 'Angelina'
Double quotation marks > "Angelina"
Triple single quotation marks > '''Angelina'''
"""
# Triple double quotation marks > """Angelina"""

#data input
#print('What\'s your name? ')
#name = input()
name = input('What\'s your name? ')

#data output
#print('Welcome, %s' % name) > python 2.x
#print('Welcome, {0}'.format(name)) >  python 3.x
print(f'Welcome, {name}!')

#data input
#print('How old are you? ')
#age = input()
age = int(input('How old are you? '))

#data output
#print('%s is %s years old' % (name, age)) > python 2.x
#print('{0} is {1} years old'.format(name, age)) > python 3.x
print(f'{name} is {age} years old')

print(f'{name} was born in {2021 - age}')
