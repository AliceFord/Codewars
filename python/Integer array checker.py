# Checks if an array is made only of integers

data = []

def is_int_array(arr):

    if arr == None:
        return True

    for i in range(len(arr)):
        try:
            arr[i] = int(arr[i])
        except:
            return False
    return True


print(is_int_array(data))
