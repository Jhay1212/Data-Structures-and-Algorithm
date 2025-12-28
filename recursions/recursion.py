def sum_of_digits(n: int) -> int:
    if n <= 0:
        return False
    return n % 10 + sum_of_digits(n // 10)
    
    
print(sum_of_digits(1234))


# def print_reverse(s: str):
#     if len(s) < 0:
#         return
#     s = s[:len(s) -1]
#     print(s)
#     return print_reverse(reversed(s))



def to_n(starting: int, target: int) -> int:
    if starting == target:
        return target
    print(starting)
    return to_n(starting=starting + 1, target=target)      
print(to_n(0,5))


# def sum_to_n(n: int) -> int:
#     if n == 0:
#         return 
#     print(n)
#     return n-2 + sum_to_n(n - 1)


# print(sum_to_n(5))

def count_down(n: int):
    if n < 0:
        return
    print(n)
    return count_down(n-1)


print(count_down(5))

def f(n: int):
    if n <= 1:
        return 1
    return f(n-1) - f(n-1)

print(f(5))


def power_of_n(base, exp):
    if exp == 0: return 1()
    if exp < 0: return 1/base  * power_of_n(base, exp+1)
    return base * power_of_n(base, exp-1)
    
    
def gcd(a, b):
    if a < 0:
        a = abs(a)
    elif b < 0:
        b = abs(b)
    if b == 0: 
        return a
    return gcd(b, a%b)


def decimal_to_binary(n: int):
    assert isinstance(n, int), "N must be type of integer only"
    if n == 0:
        return 0
    print(n)
    return n % 2 + 10 * decimal_to_binary(int(n/2))
x = power_of_n(4, 3)
print(x)
print(decimal_to_binary('dasd'))