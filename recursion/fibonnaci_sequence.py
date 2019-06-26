# 1,1,2,3,5,   8,13
# base case if n=0 or 1, then it returns 1
# fib(n-1) + fib(n-2)

store = {}

def fib_amortization2(n):
    # base case
    if n == 0 or n == 1:
        return n

    # check cache
    if n in store:
        return store[n]


    #keep setting cache
    store[n] = fib_amortization2(n-1) + fib_amortization2(n-2)

    return store[n]


n = 10
cache = [None] * (n + 1)


def fib_amortization(n):
    # base case
    if n == 0 or n == 1:
        return n

    # check cache
    if cache[n] != None:
        return cache[n]


    #keep setting cache
    cache[n] = fib_amortization(n-1) + fib_amortization(n-2)

    return cache[n]



def fib_recursive(n):

    if n == 0 or n == 1:
        return n

    return fib_recursive(n-1) + fib_recursive(n-2)



def fib_iterative(n):

    a = 0
    b = 1

    for i in range(n):
        a, b = b, a + b   # 1, 1    1,2   2,3    3,5  5,8

    return a


print(fib_iterative(5))
print(fib_recursive(3))
print(fib_amortization(10))
print(fib_amortization2(12))