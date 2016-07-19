"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python
""" 

from random import randint

a = [randint(0, 10) for x in range(10)]
b = [randint(0, 10) for x in range(15)]

common_elements = set(a) & set(b) # & stands for intersection of two sets

print("The common elements between: \n{} and\n{} are \n{}"
        .format(a, b, list(common_elements)))

