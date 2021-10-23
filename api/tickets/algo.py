from .models import Section, Rank, Seat

def main(groups):
    sections = Section.objects.all()
    ranks = Rank.objects.all()
    seats = Seat.objects.all()
    seats.update(user = None)   # remove all users from their seats
    layout = []
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
            # Assign row element to the row number of the first member of the list
            row_number = seat_rank.first().row
            order = 1
            while len(seat_rank) > 0:
                if row_number == seat_rank.first().row:
                    row_ordered.append(seat_rank.first())
                    seat_rank = seat_rank.exclude(pk=seat_rank.first().pk)
                else:
                    rank_ordered.extend(row_ordered[::order])
                    order *= -1
                    row_ordered = []
                    row_number = seat_rank.first().row
            rank_ordered.extend(row_ordered[::order])
            section_ordered.append(rank_ordered)
        layout.append(section_ordered)
        i = 0
        for j in range(len(groups)):
            current_rank = max([section[i] for section in layout], key=len)
            if current_rank == 0:
                i += 1
                current_rank = max([section[i] for section in layout], key=len)
            current_section = [section for section in layout if section[i] == current_rank]
            for _ in range(groups[j]):
                current_rank[0].user == j+1
                current_rank.pop(0)
            

    # i = 0
    # for group in groups:
    #     for _ in range(group):
    #         section = max([len(section[i]) for section in layout])
    #         print(section)



    # row_number = 5
    # row_length = 5
    # seats = [None for _ in range(row_number * row_length)]
    # i = 0
    # for j in range(len(groups)):
    #     seats[i:i + groups[j]] = [(j + 1) for _ in range(groups[j])]
    #     i += groups[j]
    # seats = [seats]
    # order = 1
    # for i in range(row_number):
    #     seats.insert(-1, seats[-1][0:row_number][::order]) 
    #     del seats[-1][:row_number]
    #     order *= -1
    # del seats[-1]
    return 'All groups have been successfully placed'