"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""
# Great optimalization can be made using functools lru_cache decorator
# which remembers most recent function calls up to maxsize

# uncommment the two lines below to reap the benefits
# import functools
# @functools.lru_cache(maxsize=None)
def fibonnaci(n):
    """Recursive implementation of fibonnaci numbers"""
    if n < 2:
        return n
    return fibonnaci(n-1) + fibonnaci(n-2)

def fibonnnaci_list(number):
    """Creates a list of first n numbers in Fibonnaci sequence."""
    return [fibonnaci(n) for n in range(number + 1)]

# how to do it in one line ;)
def fibonnaci_2(number):
    """Functools reduce implementation of fibonnaci numbers"""
    from functools import reduce
    return reduce(lambda x, y: x + y, range(number + 1))
    
# Optimal Solution via python generator
def fib:
    prev, curr = 0, 1
    while True:
        yield prev
        prev, curr = curr, prev + curr

# Or some clunky fun with classes
class fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
     return self

    def __next__(self):
     self.prev, self.curr = (self.curr, self.curr + self.prev)
     return self.prev

print(fibonnaci_2(10))
print(fibonnnaci_list(10))

