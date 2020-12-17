# A program to encode a message in 0's

data = "C"


def send(s):

    tempS = ""
    tempBinaryArray = []
    binaryArray = []

    for i in range(len(s)):
        tempS = ord(s[i])
        tempS = bin(tempS)
        tempS = tempS[2:]
        tempBinaryArray = list(tempS)
        for j in range(len(tempBinaryArray)):
            binaryArray.append(tempBinaryArray[j])

    binaryArray.append('2')

    prevData = '-1'
    nextData = '1'
    first = '1'

    answer = ""

    for i in range(len(binaryArray)-1):

        if i == 0:
            pass
        else:
            prevData = binaryArray[i-1]

        nextData = binaryArray[i+1]

        if binaryArray[i] == '0':
            if binaryArray[i] != prevData:
                answer += "00 "
                if binaryArray[i] != nextData:
                    answer += "0 "

            if binaryArray[i] == prevData:
                if binaryArray[i] == nextData:
                    answer += "0"
                if binaryArray[i] != prevData:
                    answer += "0 "

        if binaryArray[i] == '1':
            if binaryArray[i] != prevData:
                answer += "0 "
                if binaryArray[i] != nextData:
                    answer += "0 "

            if binaryArray[i] == prevData:
                if binaryArray[i] == nextData:
                    answer += "0"
                if binaryArray[i] != prevData:
                    answer += "0 "



        prevData = binaryArray[i]

    return binaryArray, answer


print(send(data))
