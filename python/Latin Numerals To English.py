# A program to turn Latin numerals into English Characters

data = "VI"
total = 0


def string_flip(flipData):
    dataLength = len(flipData)
    dataFlip = flipData[dataLength::-1]
    flipData = dataFlip
    return flipData


data = string_flip(data)
data = list(data)


for i in range(10):
    data.append(0)

print(data)

i = 0


if data[i] == "I":
    if data[i+1] == "I":
        if data[i+2] == "I":
            total += 3
        else:
            total += 2
    else:
        total += 1
else:
    total += 0

i = total

if data[i] == "V":
    if data[i+1] == "I":
        total += 4
        i += 2
    else:
        total += 5
        i += 1
else:
    pass

# LOOP INSIDE 99!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

print(i)
print(total)
