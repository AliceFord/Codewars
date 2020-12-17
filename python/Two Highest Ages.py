# A program to output the highest ages from a set of data

data = [1, 5, 87, 45, 8, 8]


def two_oldest_ages(ages):

    oldest = -1
    secondOldest = -1
    answer = []

    for i in range(len(ages)):
        if ages[i] > secondOldest and ages[i] > oldest:
            oldest = ages[i]
        elif secondOldest < ages[i] < oldest:
            secondOldest = ages[i]
        else:
            pass

    answer.append(secondOldest)
    answer.append(oldest)

    return answer


print(two_oldest_ages(data))
