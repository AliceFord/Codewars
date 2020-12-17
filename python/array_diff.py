def array_diff(a, b):
     
    for item in b:
        try:
            a.remove(item)
            a.remove(item)
        except: pass
    return a

print(array_diff([1,2], [1]))