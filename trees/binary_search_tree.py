from sys import argv


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self, first_value):
        self.root = Node(first_value)

    def insert(self, value):
        pass

    def search(self, target):
        return False


def main(args):
    # Set up tree
    tree = BST(4)

    # Insert elements
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)

    # Check search
    # Should be True
    print(tree.search(4))
    # Should be False
    print(tree.search(6))


if __name__ == "__main__":
    args = argv
    main(args)
