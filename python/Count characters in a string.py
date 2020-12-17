# A program to count characters in a string

data = 'dsd'


def count(string):

    if len(string) == 0:
        return {}

    strn = list(string)

    finalData = {}

    for i in range(len(string)):

        try:
            finalData[strn[i]] += 1

        except:
            finalData[strn[i]] = 1

    return finalData


print(count(data))
