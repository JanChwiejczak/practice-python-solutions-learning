from datetime import date

name = raw_input('Please enter your name: ')
age = int(raw_input('How old are you? '))
times = int(raw_input('How many times would you like to hear when you turn 100? '))

year = date.today().year
turns100 = year + (100 - age)

for i in range(0,times):
    print('{} you will turn 100 years old in {}!'.format(name,turns100))
