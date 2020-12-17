def is_interesting(number, awesome_phrases):
    if number < 98: return 0
    round = 2
    for i in range(3):
        # for j in range(len(str(number))):
        #     temp = number // 10
        #     if temp == int(str(number)[j]):
        #         return round
        c = sorted(number)
        if not(''.join([str(i) for i in number]) > ''.join([str(i) for i in c])):
            return 2


print(is_interesting(1336, [1337, 256]))
