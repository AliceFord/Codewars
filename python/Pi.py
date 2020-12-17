'''
# A program to calculate pi

piAccuracy = int(input('Input Pi Accuracy: ')) * 1000000

piQuarter = 1

for i in range(1, piAccuracy):

    piQuarter = piQuarter - ((i % 2) * 2 - 1) * (1 / (i*2+1))  # 1st part creates +-1 for odd/even and the 2nd part adds
    # / subtracts the fraction.

print(str(piQuarter * 4))
'''

# PRO PROGRAM
''''
from math import factorial
from decimal import Decimal, getcontext

getcontext().prec=100


def calc(n):
    t= Decimal(0)
    pi = Decimal(0)
    deno= Decimal(0)
    k = 0
    for k in range(n):
        t = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
        deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
        pi += Decimal(t)/Decimal(deno)
    pi = pi * Decimal(12)/Decimal(640320**(1.5))
    pi = 1/pi
    return pi

print(calc(100))

'''

# My PROgram

from decimal import Decimal, getcontext
getcontext().prec=10000
print(sum(1/Decimal(16)**k *
          (Decimal(4)/(8*k+1) -
           Decimal(2)/(8*k+4) -
           Decimal(1)/(8*k+5) -
           Decimal(1)/(8*k+6)) for k in range(1000)))
