# A program to encode a message in 0's

data = "C"


def send(s):

    binaryArray = []

    for i in range(len(s)):
        tempBinaryArray = list(bin(ord(s[i]))[2:])  # Turns the data from letters to binary values based on 7-bit ASCII
        if s == " ":
            tempBinaryArray += "0"
        for j in range(len(tempBinaryArray)):
            binaryArray.append(tempBinaryArray[j])

    binaryArray.append(tempBinaryArray[len(tempBinaryArray)-1])

    prevData = "-1"

    answer = ""

    for i in range(len(binaryArray)):

        if binaryArray[i] == '1' and i != 0:
            if binaryArray[i] != prevData:
                answer += "0"
                answer += " 0 "

            if binaryArray[i] == prevData:
                answer += "0"

        if binaryArray[i] == '1' and i == 0:
            if binaryArray[i] != prevData:
                answer += " 0 "

        if binaryArray[i] == '0' and i != 0:
            if binaryArray[i] != prevData:
                answer += "0"
                answer += " 00 "

            if binaryArray[i] == prevData:
                answer += "0"

        if binaryArray[i] == '0' and i == 0:
            if binaryArray[i] != prevData:
                answer += " 00 "

        prevData = binaryArray[i]

    answer = answer[1:]

    if answer == "0 0 00 0000 0 00 00 0 0 0 00 00000":
        return True
    else:
        return False, answer


print(send(data))
