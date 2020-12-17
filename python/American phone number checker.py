# A program to test if an american phone number is legitimate

data = "(123) 456-7890"
import tMath
def validPhoneNumber(phoneNumber):

    splitData = list(phoneNumber)

    if splitData[0] == "(" and splitData[4] == ")" and splitData[5] == " " and splitData[9] == "-" and len(phoneNumber) == 14:
        return True
    else:
        return False


print(validPhoneNumber(data))
