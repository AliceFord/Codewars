def next_bigger(n):
    for i in range(len(str(n))):
        changedN = n[i + 1] + n[i] + n[:i]

        return changedN


print(next_bigger(100))
