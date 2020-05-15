"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""


class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000

    def store(self, string):
        """Input a string that's stored in
        the table."""
        hash_value = self.calculate_hash_value(string)
        self.table[hash_value] = string

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hash_value = self.calculate_hash_value(string)
        return hash_value if self.table[hash_value] is not None else -1

    def calculate_hash_value(self, string):
        """Helper function to calculate a
        hash value from a string."""
        return (ord(string[0]) * 100 + ord(string[1])) % len(self.table)


def main():
    # Setup
    hash_table = HashTable()

    # Test calculate_hash_value
    # Should be 8568
    print(hash_table.calculate_hash_value('DOR BAR'))

    # Test lookup edge case
    # Should be -1
    print(hash_table.lookup('DOR BAR'))

    # Test store
    hash_table.store('DOR BAR')
    # Should be 8568
    print(hash_table.lookup('DOR BAR'))

    # Test store edge case
    hash_table.store('DOR BARR')
    # Should be 8568
    print(hash_table.lookup('DOR BARR'))


if __name__ == "__main__":
    main()
