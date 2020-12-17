# A program to see which person survives Josephus permutation

people = 7
likelihood = 3


def josephus_survivor(n,k):

    data = []

    for i in range(n):
        data.append(n-i)

    data.sort()

    numToLeave = 0

    for i in range(3):
        
        for j in range(k):
            numToLeave += data[numToLeave]

        if numToLeave > n:
            numToLeave = numToLeave % n

        data.remove(numToLeave)

        n = len(data)


    return data,numToLeave


print(josephus_survivor(7,3))