from random import randint


def highLo():
    compNum = randint(1, 100)
    for i in range(10):
        humanNum = int(input("Input a number between 1 and 100 to guess what the computer is thinking: "))
        print(compNum)
        if humanNum > compNum:
            print("Too high!")
        elif humanNum < compNum:
            print("Too low!")
        elif humanNum == compNum:
            print("Perfect! It took you " + str(i + 1) + " guesses!")
            return None
    print("You didn't get it! The number was " + str(compNum) + ".")


if __name__ == "__main__":
    highLo()
