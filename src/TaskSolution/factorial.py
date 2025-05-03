from math import factorial
from src.TaskSolution.help_functions import time_memory_used

@time_memory_used
def factorial_math():
    print(factorial(400))

@time_memory_used 
def my_factorial_1():
    print(factorial_1(400))

@time_memory_used
def my_factorial_2():
    print(factorial_2(400))

def factorial_1(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    

def factorial_2(n: int) -> int:
    result = 1
    for i in range(2,n + 1):
        result *= i
    return result    
    