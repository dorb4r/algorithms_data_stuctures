from sys import argv


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self, first_value):
        self.root = Node(first_value)

    def _insert(self, start, value):
        if start.value < value:
            if start.right is None:
                start.right = Node(value)
            else:
                return self._insert(start.right, value)
        else:
            if start.left is None:
                start.left = Node(value)
            else:
                return self._insert(start.left, value)

    def insert(self, value):
        """
        Insert a value in the correct place of the binary tree
        :param value:
        :return:
        """
        self._insert(self.root, value)

    def search(self, target):
        """

        :param target:
        :return: True if the value is in the tree False if not
        """
        return self._search(self.root, target)

    def _search(self, start, target):
        if start:
            if start.value > target:
                return self._search(start.left, target)
            elif start.value < target:
                return self._search(start.right, target)
            else:
                return True
        else:
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
