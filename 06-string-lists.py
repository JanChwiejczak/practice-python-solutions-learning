"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
"""

string_to_check = raw_input('Hi please give me a word, I will check whether it is a palindrome: ')

string_to_check = string_to_check.lower() # Convert to lowercase

if string_to_check == string_to_check[::-1]: # [::-1] is an example of list slicing
    print('{} is a palindrome.'.format(string_to_check))
else:
    print('{} is not a palindrome.'.format(string_to_check))

