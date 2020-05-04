from sys import argv


class Percolation:
    # // creates n-by-n grid, with all sites initially blocked
    def __init__(self, n: int):
        pass

    # // opens the site (row, col) if it is not open already
    def open(self, row: int, col: int):
        pass

    # // is the site (row, col) open?
    def is_open(self, row: int, col: int):
        pass

    # // is the site (row, col) full?
    def is_full(self, row: int, col: int):
        pass

    # // returns the number of open sites
    def number_of_open_sites(self):
        pass

    # // does the system percolate?
    def percolates(self):
        pass


# // test client (optional)
def main(args):
    pass


if __name__ == "__main__":
    main(argv)
