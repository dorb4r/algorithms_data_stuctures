from sys import argv


def bubble_sort(array):
    return []


def main():
    test1 = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    test2 = [6, 3, 22, 44, 14, 2, 34, 50]

    result = bubble_sort(test1)
    assert result == [1, 3, 4, 6, 9, 14, 20, 21, 21, 25]

    result = bubble_sort(test2)
    assert result == [2, 3, 6, 14, 22, 34, 44, 50]


if __name__ == "__main__":
    args = argv
    main()
