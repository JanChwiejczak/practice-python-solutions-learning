"""
This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.

Take two lists, say for example these two:

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. 
"""

from random import sample 

a = sample(range(30), 15)
b = sample(range(30), 16)
common_elements = set(a) & set(b)
common_elements2 = set([i for i in a if i in b])

print(a)
print(b)
print(common_elements)
print(common_elements == common_elements2)

