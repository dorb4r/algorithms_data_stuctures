"""
Social network connectivity. Given a social network containing N members and a
log file containing M timestamps at which times pairs of members formed friendships,
design an algorithm to determine the earliest time at which all members are connected
(i.e., every member is a friend of a friend of a friend ... of a friend). Assume that
the log file is sorted by timestamp and that friendship is an equivalence relation.
The running time of your algorithm should be m
log n or better and use extra space proportional to N.
"""


class SocialNetwork:
    def __init__(self, num_of_members):
        # Create an array of friends to work with
        self.members = list(range(0, num_of_members))
        self.members_union = 0

    def __root(self, member_index):
        pass

    def form_friendship(self, member_a, member_b):
        pass

    def are_connected(self, member_a, member_b):
        pass
