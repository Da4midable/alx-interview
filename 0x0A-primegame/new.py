#!/usr/bin/python3



def productOf(num: int, den: int):
    if ifFloat(num, den) == True:
        return False
    c = num / den
    if c == 1:
        return True
    num = c
    return productOf(num, den)

def ifFloat(a, b):
    result = a / b
    return isinstance(result, float) and not result.is_integer()


def is_product(num1: int, num2: int):
    return num1 % num2 == 0 or num2 % num1 == 0

def pop_productOf(arr, num):
    return [x for x in arr if not is_product(x, num)]



a = [1, 21, 2, 4, 18, 35, 14, 7, 700, 19, 800, 805, 21, 33, 23, 44, 3, 900]
b = 2
c = pop_productOf(a, b)
print(c)
