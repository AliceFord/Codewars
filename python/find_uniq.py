def find_uniq(arr):
    for i in range(len(arr)):
        arr[i] = arr[i].lower()
    return arr


print(find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]))
