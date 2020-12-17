# Product of consecutive fibonacci numbers

data = 4895


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


def productFib(prod):
    fibNum = 0
    while True:
        fibNum += 1
        sum = fib(fibNum)*fib(fibNum+1)
        if sum < prod:
            pass
        if sum > prod:
            return [fib(fibNum),fib(fibNum+1),False]
        if sum == prod:
            return [fib(fibNum),fib(fibNum+1),True]


print(productFib(data))
