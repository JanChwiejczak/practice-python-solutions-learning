def less_than(list, x):
    """Takes a list of numbers and returns all numbers smaller than x"""
    return [y for y in list if y < x]

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print(less_than(a, 5))