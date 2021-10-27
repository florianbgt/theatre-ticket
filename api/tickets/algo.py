def main(sections, ranks, seats, groups):
    # Remove all users from their seats
    seats.update(user = None)
    layout = []
    # Iterate over each section
    for section in sections:
        #Get all seats in the section
        seat_section = seats.filter(section=section)
        section_ordered = []
        for rank in ranks:
            # Get all seat of the specific rank in the section and sort them
            seat_rank = seat_section.filter(rank=rank).order_by('row', 'number')
            # If no seat with rank, append empty list and exit loop
            if len(seat_rank) == 0:
                section_ordered.append([])
                continue
            rank_ordered = []
            row_ordered = []
            row_number = seat_rank.first().row
            # Order 1 == best rank
            order = 1
            # loop until no seat in seat_rank
            while len(seat_rank) > 0:
                # if row # == first item row #, append to list and remove seat
                if row_number == seat_rank.first().row:
                    row_ordered.append(seat_rank.first())
                    seat_rank = seat_rank.exclude(pk=seat_rank.first().pk)
                # else, end of the row, append the row_ordered to the rank ordered and reverse 1/2 time
                else:
                    rank_ordered.extend(row_ordered[::order])
                    order *= -1
                    row_ordered = []
                    row_number = seat_rank.first().row
            rank_ordered.extend(row_ordered[::order])
            section_ordered.append(rank_ordered)
        layout.append(section_ordered)
    # Layout is done at this point
    
    # Asssign seats to user from here
    for j in range(len(groups)):
        rank = 0
        # Get the rank section with the most seats available
        current_rank = max([section[rank] for section in layout], key=len)
        # If no seat available with current rank, get next rank
        while len(current_rank) == 0:
            rank += 1
            current_rank = max([section[rank] for section in layout], key=len)
        # get current section
        current_section = [section for section in layout if section[rank] == current_rank][0]
        for _ in range(groups[j]):
            # If no seat in current rank, place users in next rank but same section so they stay with their group
            if len(current_rank) == 0:
                current_rank = current_section[rank+1]
                # If no seat in current section, place user in other section but same rank
                rank = -1
                while len(current_rank) == 0:
                    rank += 1
                    current_rank = max([section[rank] for section in layout], key=len)
            current_rank[0].user = j+1
            current_rank[0].save()
            current_rank.pop(0)