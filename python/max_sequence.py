def max_sequence(arr):
    sum = -100
    if not arr: return 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            temp = 0
            subArray = arr[i:j+1]
            for k in range(len(subArray)):
                temp += subArray[k]
            if temp > sum: sum = temp

    return sum


print(max_sequence([1, 2, 3]))
