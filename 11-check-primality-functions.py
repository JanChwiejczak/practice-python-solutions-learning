"""
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.).
""" 
import sys

def get_number(question='Please provide a number: '):
    try:
        return int(input(question))
    except ValueError:
        print('This is not a number.')
        sys.exit()

def is_prime(number):
    if number in range(2):
        return False
    for x in range(2, number):
        if number % x == 0:
            return False
    return True
    
print(is_prime(get_number()))

