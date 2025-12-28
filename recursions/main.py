from typing import List


def first_method():
    second_method()
    print("I am first method")
    
def second_method():
    third_method()
    print("I am second method")
    
def third_method():
    fourth_method()
    print("I am third method")
    
def fourth_method():
    print("I am final method")
    
    
    
first_method()


def factorial(n: int) -> int:
    if n == 0:
        return "Factorial does not exist for negative numbers"
    if n == 1:
        return 1
    return n * factorial(n - 1)



def power_of_two(n: int | float) -> int:
    if n == 0:
        return 1
    
    
print(factorial(5))

def fibonacci(n: int) -> int:
    if n == 1 or n == 0: 
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5), "fib")

def product_of_array(n: List[int]) -> int | float:
    if not len(n):
        return 1
    return n[0] * product_of_array(n[1:])



def recursive_range(n: int):
    if n <= 0:
        return n
    return n + recursive_range(n-1)
print(product_of_array([1, 2,3 ]))
print(recursive_range(10))