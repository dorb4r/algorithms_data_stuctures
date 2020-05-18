from sys import argv


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, first_value):
        self.root = Node(first_value)


def main(args):
    pass


if __name__ == "__main__":
    args = argv
    main(args)
