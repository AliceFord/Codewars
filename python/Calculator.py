import operator
class Calculator(object):
    def evaluate(self, string):
        intArr = string.split(" ")
        ans = 0
        for i in intArr:
            if type(i) is int:
                ans += int(i)

        print(intArr)


print(Calculator().evaluate("2 / 2 + 3 * 4 - 6"))
