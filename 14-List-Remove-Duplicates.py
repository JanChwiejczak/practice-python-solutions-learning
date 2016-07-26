"""
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""

def remove_duplicates(a_list):
    return list(set(a_list))

def remove_duplicates_2(a_list):
    unique_list = []
    for entry in a_list:
        if entry not in unique_list:
            unique_list.append(entry)
    return unique_list

a_list = list(range(10)) * 2
print(remove_duplicates(a_list) == remove_duplicates_2(a_list))

