# Given a list of “groups of users” per rank (basically sizes, e.g. (1, 3, 4, 4, 5, 1, 2, 4) in a
# specific order,
# try to place the users in their seats, e.g.
# 1 2 2 2 3 3 3 3
# 5 5 5 5 4 4 4 4
# 5 6 7 7 8 8 8 8
# So the group of size 1 at index 1 gets the frontmost left seat. Then the group at index 2
# of 3 people next to it, until the
# row fills and wraps to the next row and fills in the other direction.
# You can assume that sum(groups_of_users_for_rank) <= seats_in_that_rank
# Bonus options:
# ● Take preferences into account based on seat properties. E.g. (“aisle”, 2) would
# mean a group of 2 where one of the members wishes to be near the aisle
# ● Allow seats to be blocked (e.g. for technical purposes). This means a group
# should not be split across such a block
# ● Implement the seating algorithm in a non-blocking way, e.g. task, async, so it can
# be called using an API.

def main(groups):
    row_number = 5
    row_length = 5
    seats = [None for _ in range(row_number * row_length)]
    i = 0
    for j in range(len(groups)):
        seats[i:i + groups[j]] = [(j + 1) for _ in range(groups[j])]
        i += groups[j]
    print(seats)
    seats = [seats]
    for i in range(row_number):
        seats.insert(0, seats[-1][0:row_number]) 
        del seats[-1][-row_number:]
    print(seats)

print(main([5, 5, 5, 5, 3]))