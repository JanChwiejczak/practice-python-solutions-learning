def is_divisible(number, divisor):
    if number % divisor == 0:
        return True
    else:
        return False
        
number = int(raw_input('What number would you like to test divisibility for? '))
divisor = int(raw_input('What would you like to divide by? '))

if is_divisible(number, divisor):
    print('{} is divisible by {}'.format(number, divisor))
else:
    print('{} does not divide by {}'.format(number, divisor))