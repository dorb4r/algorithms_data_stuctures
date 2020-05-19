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
        """
        Insert a value in the correct place of the binary tree
        :param value:
        :return:
        """
        pass

    def search(self, target):
        """

        :param target:
        :return: True if the value is in the tree False if not
        """
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
