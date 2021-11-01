# Main file, creation date 17/12/20, newest file of this date, the muddled files are all older


def calculate(expression):
    ALLOWED_CHARS = ['.','0','1','2','3','4','5','6','7','8','9','+','-','*','$']

    def operatorCode():
        global onNewNum, currentNum, newNum
        if onNewNum:
            if currentOperator == 0:
                currentNum = str(float(currentNum) + float(newNum))
            elif currentOperator == 1:
                currentNum = str(float(currentNum) - float(newNum))
            elif currentOperator == 2:
                currentNum = str(float(currentNum) * float(newNum))
            if currentOperator == 3:
                currentNum = str(float(currentNum) / float(newNum))

        onNewNum = True

    for c in expression:
        if c not in ALLOWED_CHARS:
            return '400: Bad request'

    currentNum = ''
    newNum = ''
    onNewNum = False
    currentOperator = -1 # 0: +, 1: -, 2: *, 3: /
    for c in expression:
        if 46 <= ord(c) <= 57:
            if not onNewNum:
                currentNum += c
            else:
                newNum += c
        elif ord(c) == 43:
            currentOperator = 0
            operatorCode()
        elif ord(c) == 45:
            currentOperator = 1
            operatorCode()
        elif ord(c) == 42:
            currentOperator = 2
            operatorCode()
        elif ord(c) == 36:
            currentOperator = 3
            operatorCode()
        print(currentNum)
    operatorCode()
    return currentNum



if __name__ == '__main__':
    print(calculate("10+5"))
