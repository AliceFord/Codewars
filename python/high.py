def high(x):
    x = x.split(" ")
    output = [0, ""]
    for i in x:
        temp = 0
        for j in list(i):
            temp += (ord(j) - 96)
        if temp > output[0]: 
            output[0] = temp
            output[1] = i
    return output[1];

print(high('man i need a ubud up to taxi'))