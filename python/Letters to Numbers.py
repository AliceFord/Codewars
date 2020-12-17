# A program to turn letters into numbers and mathematical functions

data1 = "iiisdoso"


def parse(data):

    number = 0
    finalList = []

    dataList = list(data)

    for i in range(len(data)):

        if dataList[i] == "i":
            number += 1

        if dataList[i] == "d":
            number -= 1

        if dataList[i] == "s":
            number **= 2

        if dataList[i] == "o":
            finalList.append(number)

    return finalList


print(parse(data1))
