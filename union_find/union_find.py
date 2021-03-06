from sys import argv


class UnionFind:
    def __init__(self, data_size: int):
        # TODO - Convert this to a NumPy array
        self.id = list(range(0, data_size))

    def is_connected(self, object_a: int, object_b: int):
        return self.__root(object_a) == self.__root(object_b)

    def union(self, object_a: int, object_b: int):
        a_root = self.__root(object_a)
        b_root = self.__root(object_b)
        self.id[a_root] = b_root

    def __root(self, index):
        while index != self.id[index]:
            index = self.id[index]

        return index


# def test():
#     union_find = UnionFind(10)
#     union_find.union(1, 2)


def main(args):
    with open(args[1]) as input_file:
        is_initialized = False
        union_find = None
        for line in input_file:
            # Initialize the UnionFind object
            if is_initialized is False:
                union_find = UnionFind(int(line))
                is_initialized = True
            else:
                points = line.split(" ")
                point_a = int(points[0])
                point_b = int(points[1])

                if union_find.is_connected(point_a, point_b):
                    union_find.union(point_a, point_b)
                    print(f"{point_a} {point_b}")


if __name__ == "__main__":
    args = argv
    main(args)
    # test()
