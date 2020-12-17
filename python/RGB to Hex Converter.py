# A program to convert an RGB value to a hexadecimal one

r = 167
g = 0
b = 0

data = ["10 A", "11 B", "12 C", "13 D", "14 E", "15 F"]

rAnswer = ()
gAnswer = ()
bAnswer = ()

for i in range(1):
    rAnswer = (r // 16, r % 16)
    gAnswer = (g // 16, g % 16)
    bAnswer = (b // 16, b % 16)
    for d in range(2):
        if rAnswer[d] == 10:
            for p in range(6):
                if rAnswer[d] == data[p][:2]:
                    rAnswer = data[p][2:]
print(rAnswer, gAnswer, bAnswer)
