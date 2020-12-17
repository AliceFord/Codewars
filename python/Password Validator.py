# A program to validate a password

data = "Abcd1234"

def password(string):

    dataList = list(string)

    if len(string) < 8:
        return False

    if string.upper() == string:
        return False

    if string.lower() == string:
        return False

    for i in range(len(string)):
        if dataList[i].isdigit():
            return True
        else:
            pass

    return False


print(password(data))