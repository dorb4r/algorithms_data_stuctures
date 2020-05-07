def binary_search(input_list, value):
    low = 0
    high = len(input_list) - 1

    while low <= high:
        mid = int((high - low) / 2 + low)

        if input_list[mid] > value:
            high = mid - 1
        elif input_list[mid] < value:
            low = mid + 1
        else:
            return mid
    return -1


def main():
    input_array = [1, 5, 6, 7, 9, 22, 34, 55]
    assert binary_search(input_array, 9) == 4
    assert binary_search(input_array, 80) == -1
    assert binary_search(input_array, 55) == 7


if __name__ == "__main__":
    main()
