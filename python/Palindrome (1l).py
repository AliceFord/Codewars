def palindrome(n, c): return c.ljust(n-len(c),c[0])+c[::-2]

print(palindrome(13, "ab"))