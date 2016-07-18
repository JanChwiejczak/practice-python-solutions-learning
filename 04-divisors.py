"""Create a program that asks the user for a number and then prints out a list of all the divisors of that number

http://www.practicepython.org/exercise/2014/02/26/04-divisors.html
"""

try:
    number = int(raw_input('Please provide an integer: '))
except ValueError:
    print('You must provide a valid integer')


divisors = [i for i in range(2,number+1) if number % i == 0]

print('{} can by divided by {}'.format(number, divisors))