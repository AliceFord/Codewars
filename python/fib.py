import sys

def fib(n):
	if n == 0: return 0
	elif n == 1: return 1
	elif n < 0:
		return fib(n + 2) - fib(n + 1)
	return fib(n - 1) + fib(n - 2)


from math import sqrt
import decimal
decimal.getcontext().prec = decimal.getcontext().Emax
def F(n):
	return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))


print(F(2000000))
