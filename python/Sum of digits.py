# A program to find the sum of some digits


def digital_root(n):
    n = list(str(n))
    ans = 0
    for i in range(len(n)):
        ans += int(n[i])

    ans = list(str(ans))
    print(int(''.join(ans)))  # TODO: REMOVE
    if int(''.join(ans)) >= 10:
        digital_root(int(''.join(ans)))

    if int(''.join(n)) < 10:
        return int(''.join(ans))


print(digital_root(1232434))
