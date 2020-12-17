# A program to find all multiples of 3 and 5 below 1000

total = 0

for i in range(1, 334):
    total += i * 3
    print(total)

for i in range(1,200):
    total += i * 5
    print(total)

print(total)