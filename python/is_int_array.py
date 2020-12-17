def is_int_array(arr):
    if arr == None or arr == "": return False
    for i in arr:
        if not(i == int(i)): return False
    return True

print(is_int_array([1, 2, 3, 4]))