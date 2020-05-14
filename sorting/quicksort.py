from sys import argv

"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# Function to do Quick sort
def quick_sort(arr, low=None, high=None):
    if low is None and high is None:
        low = 0
        high = len(arr) - 1

    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

        return arr


def main(args):
    test1 = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    test2 = [6, 3, 22, 44, 14, 2, 34, 50]

    result = quick_sort(test1)
    assert result == [1, 3, 4, 6, 9, 14, 20, 21, 21, 25]

    result = quick_sort(test2)
    assert result == [2, 3, 6, 14, 22, 34, 44, 50]


if __name__ == "__main__":
    args = argv
    main(args)
