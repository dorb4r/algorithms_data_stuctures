from sys import argv


class Percolation:
    # // creates n-by-n grid, with all sites initially blocked
    def __init__(self, n: int):
        self.grid = [[None for x in list(range(0, n))] for x in list(range(0, n))]

    # // opens the site (row, col) if it is not open already
    def open(self, row: int, col: int):
        self.grid[row][col] = 1

    # // is the site (row, col) open?
    def is_open(self, row: int, col: int):
        return self.grid[row][col] is not None

    # // is the site (row, col) full?
    def is_full(self, row: int, col: int):
        pass

    # // returns the number of open sites
    def number_of_open_sites(self):
        pass

    # // does the system percolate?
    def percolates(self):
        pass

    def __root(self, index):
        while index != self.id[index]:
            index = self.id[index]

        return index


# // test client (optional)
def main(args):
    percolation = Percolation(3)
    print(percolation.grid)
    percolation.open(0, 0)
    print(percolation.grid)


if __name__ == "__main__":
    main(argv)
