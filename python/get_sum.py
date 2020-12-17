def get_sum(a,b):
    ans = 0
    if a < b:
        while (a <= b):
            ans += a
            a += 1
    else:
        while (a >= b):
            ans += a
            a -= 1
    return ans

print(get_sum(1, 3))