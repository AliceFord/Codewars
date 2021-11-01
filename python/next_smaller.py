def next_smaller(n):
    for i in range(n, 0, -1):
        if len(str(i)) == len(str(n)) and sorted(str(i)) == sorted(str(n)) and i < n:
            return i

def next_bigger(n):
    # i = n
    # while True:
    #     if len(str(i)) == len(str(n)) and sorted(str(i)) == sorted(str(n)) and i > n:
    #         return i
    #     elif len(str(i)) > len(str(n)): return -1
    #     i += 1
    nPerms = []
    for i in range(len(str(n))**2):
        temp = str(n)[i//len(str(n)):i//len(str(n))+1]
        print(temp)
        nPerms.append(str(n)[:i%len(str(n))] + temp + str(n)[i%len(str(n))+1:])
    return nPerms


#print(next_smaller(123456789))
print(next_bigger(123))
