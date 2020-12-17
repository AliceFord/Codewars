# A program to see if numbers are consecutive

data = [1,2,3,4,5,6,8,9,10]


def first_non_consecutive(arr):

    for i in range(len(arr)):
        if arr[i] < arr[len(arr)-1]:
            if arr[i+1] - arr[i] == 1:
                pass
            else:
               return arr[i+1]
        else:
            return None


print(first_non_consecutive(data))
