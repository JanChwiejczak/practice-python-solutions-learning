"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""
# Prefered solution
from os import urandom

def generate_password(length=24):
    return urandom(length)

# Silly solution
from random import randint, choice
from string import ascii_letters, digits, punctuation

def generate_password(length=24, strength=3):
    """Generates a password of a given length, the strentgh measures
    complexity of generated password with 1 only letters, 2 letters 
    and numbers and 3 for passwords with letters, numbers and special chars"""
   
    chars = {1: ascii_letters, 2: digits, 3: punctuation}
    password = ''
    for i in range(0,length):
        password = ''.join([password, choice(chars[randint(1,strength)])])
    return password

