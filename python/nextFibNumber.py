def nextFibNumber(x):
    fibNum1 = 0
    fibNum2 = 1
    while True:
        fibNum1 += fibNum2
        if fibNum1 > x: return fibNum1
        temp = fibNum2
        fibNum1 = fibNum2
        fibNum2 = temp


print(nextFibNumber(4))
