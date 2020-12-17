# A program to increment a string by 1

data = "1foobar001"


def increment_string(strng):

    strngSplit = list(strng)

    for i in range(len(strng)):
        if not str.isdigit(strngSplit[i]):
            strngSplit.append("1")

    return strngSplit


print(increment_string(data))
