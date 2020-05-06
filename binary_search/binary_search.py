def binary_search(input_list, value):
    low = 0
    high = len(input_list) - 1

    while low <= high:
        mid = (high - low) / 2 + low

        if input_list[mid] > value:
            high = mid - 1
        elif input_list[mid] < value:
            low = mid + 1
        else:
            return value


def main():
    input_array = [1, 5, 6, 7, 9, 22, 34, 55]
    binary_search(input_array, 9)
    binary_search(input_array, 80)


if __name__ == "__main__":
    main()
