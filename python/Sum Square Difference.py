# A program to find the difference between the sum of the squares and the square of the sum

step1 = 0
step2 = 0

for i in range(1, 111):
    step1 += i ** 2

print(step1)

for i in range(1, 111):
    step2 += i

step2 **= 2

print(step2)

print(step2 - step1)
