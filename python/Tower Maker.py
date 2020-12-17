# A program to make a tower

data = 100
answer = []
test = 0
maxLength = (data*2)+1
for g in range(data):
    answer.append('')
    for i in range((data*2)):
        answer[g] += ' '
        if i+1 == data-g:
            for f in range(((g+1)*2)-1):
                answer[g] += '*'
        if maxLength == len(answer[g]):
            break

for i in range(data):
    answer[i] = answer[i][1:]
    answer[i] = answer[i][:-1]

for i in range(data):
    print(answer[i])
