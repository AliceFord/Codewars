from random import randint
from timeit import repeat


def run_sorting_algorithm(algorithm, array):

    setup_code = f'from __main__ import {algorithm}' \
        if algorithm != "sorted" else ""

    stmt = f'{algorithm}({array})'

    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    print(f'Algorithm: {algorithm}. Minimum execution time: {min(times)}')


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[i]

                already_sorted = False

        if already_sorted:
            break

    return array


def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]

        j = i - 1

        while j >= 0 and array[j] > key_item:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = key_item

    return array


def merge(left, right):
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


ARRAY_LENGTH = 10000

if __name__ == "__main__":
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    run_sorting_algorithm(algorithm="insertion_sort", array=array)
