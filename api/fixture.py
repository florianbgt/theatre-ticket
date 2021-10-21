import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','_project.settings')

import math

import django
django.setup()

from tickets.models import Section, Row, Rank, Seat

def populate():
    # Add sections
    main = Section.objects.get_or_create(name="Main", curved=True, balcony=False)[0]
    rear = Section.objects.get_or_create(name="Rear", curved=False, balcony=True)[0]
    right = Section.objects.get_or_create(name="Right", curved=False, balcony=True)[0]
    left = Section.objects.get_or_create(name="Left", curved=False, balcony=True)[0]

    # Add rows
    for i in range(1, 10+1):
        Row.objects.get_or_create(row=i, section=main)
        if i <= 3:
            Row.objects.get_or_create(row=i, section=rear)
            Row.objects.get_or_create(row=i, section=right)
            Row.objects.get_or_create(row=i, section=left)

    # Add ranks
    economy = Rank.objects.get_or_create(name="Economy", rank=1, cost=20)[0]
    premium = Rank.objects.get_or_create(name="Premium", rank=2, cost=30)[0]
    vip = Rank.objects.get_or_create(name="VIP", rank=3, cost=40)[0]

    # Add seats Main
    for i in range(1, 101):
        seat_row = Row.objects.get(section=main, row=math.ceil(i/10))
        if seat_row.row == 1:
            seat_rank = vip
        elif seat_row.row <= 3:
            seat_rank = premium
        else:
            seat_rank = economy
        Seat.objects.get_or_create(number=i, section=main, row=seat_row, rank=seat_rank)
    
    # Add seats Rear
    for i in range(101, 131):
        seat_row = Row.objects.get(section=rear, row=math.ceil((i-100)/10))
        if seat_row.row == 1:
            seat_rank = vip
        elif seat_row.row <= 3:
            seat_rank = premium
        else:
            seat_rank = economy
        Seat.objects.get_or_create(number=i, section=rear, row=seat_row, rank=seat_rank)
    
    # Add seats Right
    for i in range(131, 161):
        seat_row = Row.objects.get(section=left, row=math.ceil((i-130)/10))
        if seat_row.row == 1:
            seat_rank = vip
        elif seat_row.row <= 3:
            seat_rank = premium
        else:
            seat_rank = economy
        Seat.objects.get_or_create(number=i, section=right, row=seat_row, rank=seat_rank)

    # Add seats Left
    for i in range(161, 191):
        seat_row = Row.objects.get(section=right, row=math.ceil((i-160)/10))
        if seat_row.row == 1:
            seat_rank = vip
        elif seat_row.row <= 3:
            seat_rank = premium
        else:
            seat_rank = economy
        Seat.objects.get_or_create(number=i, section=left, row=seat_row, rank=seat_rank)


if __name__ == "__main__":
    populate()