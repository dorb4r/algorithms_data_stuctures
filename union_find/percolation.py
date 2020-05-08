from sys import argv


class Percolation:
    # // creates n-by-n grid, with all sites initially blocked
    def __init__(self, n: int):
        self.grid = [[-1 for x in list(range(0, n))] for x in list(range(0, n))]
        self.open_site_counter = 0

    # // opens the site (row, col) if it is not open already
    def open(self, row: int, col: int):
        self.grid[row][col] = 1

        if self.grid[row][col] > -1:
            self.open_site_counter += 1

    # // is the site (row, col) open?
    def is_open(self, row: int, col: int):
        return self.grid[row][col] is not None

    # // is the site (row, col) full?
    def is_full(self, row: int, col: int):
        return self.grid[row][col] > -1

    # // returns the number of open sites
    def number_of_open_sites(self):
        return self.open_site_counter

    # // does the system percolate?
    def percolates(self):
        pass

    def __root(self, row, col):
        while index != self.grid[index]:
            index = self.grid[index]

        return index


def print_matrix(grid):
    print('\n'.join([''.join([f'{item}\t\t' for item in row]) for row in grid]))
    print()


# // test client (optional)
def main(args):
    percolation = Percolation(4)
    print_matrix(percolation.grid)
    percolation.open(0, 0)
    print_matrix(percolation.grid)


if __name__ == "__main__":
    main(argv)
