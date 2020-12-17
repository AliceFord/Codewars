# A program to validate a credit card number using the Luhn algorithm

data = 2121

def validate(n):

    finalData = 0

    internalData = list(str(n))

    for g in range(len(internalData)):
        internalData[g] = int(internalData[g])

    odd = False

    if len(internalData) / 2 == int(len(internalData) / 2):
        odd = False
    else:
        odd = True

    if not odd:
        for i in range(1, int(len(internalData)/2+1.5)):
            internalData[i*2-2] = internalData[i*2-2] * 2

    elif odd:
        for i in range(int(len(internalData)/2)):
            internalData[i * 2+1] = internalData[i * 2+1] * 2

    for i in range(len(internalData)):
        if internalData[i] > 9:
            internalData[i] -= 9

    for i in range(len(internalData)):
        finalData += internalData[i]

    finalData = finalData % 10

    if finalData == 0:
        return True
    else:
        return False

print(validate(data))
