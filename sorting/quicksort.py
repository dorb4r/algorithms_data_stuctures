from sys import argv


def swap(array: list, pos1, pos2):
    array[pos1], array[pos2] = array[pos2], array[pos1]
    return array


def quick_sort(array: list):
    # sorted_array = array

    # for each (unsorted) partition
    for pos1, number in enumerate(array):
        # set first element as pivot
        print(array)
        pivot_index = 0
        pivot = array[pivot_index]

        storeIndex = pivot_index + 1
        #   for i = pivotIndex + 1 to rightmostIndex
        for pos2, target_number in enumerate(array):
            # if element[i] < element[pivot]
            if pivot > target_number:
        #       swap(i, storeIndex); storeIndex++
                swap(array, pos1, pos2)
                storeIndex += 1
            swap(array, pos1, storeIndex - 1)

    return array


def main(args):
    array = [6, 3, 22, 44, 14, 2, 34, 50]

    result = quick_sort(array)
    print(result)
    assert result == [2, 3, 6, 14, 34, 44, 50]


if __name__ == "__main__":
    args = argv
    main(args)
