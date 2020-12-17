def getCount(inputStr):
    return len([0 for i in list(inputStr.lower()) if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'])

print(getCount("abracadabra"))