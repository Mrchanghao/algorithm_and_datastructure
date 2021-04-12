'''
Using simple recursion
Using cache with recursion
Using an iterative method
Using Binet’s formula
Calculating the 1,000,000th number

'''

# 재귀
def recursiveFib(n):
    if n == 1 or n == 2:
        return 1

    return recursiveFib(n - 1) + recursiveFib(n - 2)


# recursion with recursive
from functools import lru_cache
import sys

@lru_cache()
def recursiveFibCached(n):
    if n == 1 or n == 2:
        return 1

    return recursiveFibCached(n - 1) + recursiveFibCached(n - 2)

sys.setrecursionlimit(5000)
print(recursiveFibCached(20))


# loop
def loop_fib(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b,  a + b

    return a

print(loop_fib(20))