from .models import Section, Rank, Seat

def main(groups):
    sections = Section.objects.all()
    ranks = Rank.objects.all()
    seats = Seat.objects.all()
    seats.update(user = None)   # remove all users from their seats
    layout = []
    for section in sections:
        #Get all seats in the section and order by row and number
        seat_section = seats.filter(section=section)
        section_ordered = []
        for rank in ranks:
            seat_rank = seat_section.filter(rank=rank).order_by('row', 'number')
            print(seat_rank)
            rank_ordered = []
            row_ordered = []
            print('fail here')
            row_number = seat_rank.first().row
            while len(seat_rank) > 0:
                if row_number == seat_rank.first().row:
                    row_ordered.append(seat_rank.first())
                    seat_rank = seat_rank.exclude(pk=seat_rank.first().pk)
                else:
                    rank_ordered.append(row_ordered)
                    row_ordered = []
                    row_number = seat_rank.first().row
            rank_ordered.append(row_ordered)
            section_ordered.append(rank_ordered)
        layout.append(section_ordered)
    print(layout)
        
        # row = []
        # row_number = seat_section.first().row
        # # Iterate over seat_section to map it by row
        # while len(seat_section) > 0:
        #     if row_number == seat_section.first().row:
        #         row.append(seat_section.first())
        #         seat_section = seat_section.exclude(pk=seat_section.first().pk)
        #     else:
        #         seat_section_mapped.append(row)
        #         row = []
        #         row_number = seat_section.first().row
        # seat_section_mapped.append(row)
        # layout.append(seat_section_mapped)
    print(layout)
    for group in groups:
        print(group)



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
    return []