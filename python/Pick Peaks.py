# A program to pick the peaks from an array

data = [2,1,3,1,2,2,2,2]
pick = [-1]
peak = [0]
bracesSet = {}
for i in range(len(data)):
    if data[i] > peak[0]:
        peak[0] = data[i]
        pick[0] = i

bracesSet.add("pos:", peak[0])
bracesSet.add("pos:", pick[0])
print(bracesSet)