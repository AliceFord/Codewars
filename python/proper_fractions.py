from fractions import Fraction

def proper_fractions(n):
    ans = 0
    for i in range(1, n + 1):
        if str(Fraction(i, n)) == "{}/{}".format(i, n): ans += 1
    return ans

def fracTest(n):
    return len([1 for i in range(1, n + 1) if str(Fraction(i, n)) == "{}/{}".format(i, n)])

print(proper_fractions(15))
print(fracTest(15))