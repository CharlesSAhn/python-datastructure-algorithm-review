# 1,1,2,3,5,   8,13
# base case if n=0 or 1, then it returns 1
# fib(n-1) + fib(n-2)



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