"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""
def fibonnaci(n):
    """Recursive implementation of fibonnaci numbers"""
    if n < 2:
        return n
    return fibonnaci(n-1) + fibonnaci(n-2)

def fibonnnci_list(number):
    """Creates a list of first n numbers in Fibonnaci sequence."""
    return [fibonnaci(n) for n in range(number + 1)]

print(fibonnnci_list(10))

