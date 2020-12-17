# A program to find which strings in an array are substrings of strings in another array

array1 = ["arp", "live", "strong"]
array2 = ["lively", "alive", "harp", "sharp", "armstrong"]
answer = []
for i in range(len(array1)):
    for g in range(len(array2)):
        if array1[i] in array2[g]:
            answer.append(array1[i])

for i in range(len(answer)):
    for g in range(len(answer)):
        try:
            if answer[i] == answer[g] and i != g:
                del answer[g]
        except:
            pass
answer.sort()
print(answer)
