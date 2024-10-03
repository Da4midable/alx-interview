#!/usr/bin/python3

def isWinner(x, nums):
    player1 = 'Maria'
    player2 = 'Ben'
    n = max(nums)
    n = [x for x in range(n + 1) if x > 0]
    print('This is now ', n)

    for i in range(x):
        if isPrime(n[i]) and n[i] >= 2:
            pop_productOf(n, n[i])
            print(n, 'is popped!')
            c = [a for a in nums if isPrime(a)]
            print('This is the first', c)
            
            if not c:
                return player1
            if c:
                pop_productOf(nums, nums[i])
                d = [a for a in nums if isPrime(a)]
                print('This is', d)
                if not d:
                    return player2
    return None



def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n+1):
        if prime[p]:
            print(p)


def is_product(num1: int, num2: int):
    return num1 % num2 == 0 or num2 % num1 == 0

def pop_productOf(arr, num):
    return [x for x in arr if not is_product(x, num)]


    