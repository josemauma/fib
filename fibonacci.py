"""
    Calculates the nth Fibonacci number.
    
    The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, 
    usually starting with 0 and 1. That is, F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n > 1.
    
    Args:
        n (int): The position in the Fibonacci sequence to calculate. Must be a non-negative integer.
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If the input is a negative integer.
"""


import argparse
import sys


def fibonaccci_iterative(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonaccci_iterative(n-1) + fibonaccci_iterative(n-2)

if __name__ == '--main--':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('nth', type=int, help='The position in the Fibonacci sequence to calculate.')
    #parser.add_argument('-c','--count')
    #parser.add_argument('-v','--verbose', action='store_true')
    args = parser.parse_args()
    
    result = fibonaccci_iterative(args.nth)
    print(result)