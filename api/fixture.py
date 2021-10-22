import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','_project.settings')

import math

import django
django.setup()

from django.core.management import call_command
from django.conf import settings

from tickets.models import Section, Rank, Seat
from django.contrib.auth.models import User

def populate():
    # Add sections
    main = Section.objects.get_or_create(name="Main", curved=True, balcony=False)[0]
    rear = Section.objects.get_or_create(name="Rear", curved=False, balcony=True)[0]
    right = Section.objects.get_or_create(name="Right", curved=False, balcony=True)[0]
    left = Section.objects.get_or_create(name="Left", curved=False, balcony=True)[0]

    # Add ranks
    vip = Rank.objects.get_or_create(name="VIP", rank=1)[0]
    premium = Rank.objects.get_or_create(name="Premium", rank=2)[0]
    economy = Rank.objects.get_or_create(name="Economy", rank=3)[0]

    # Add seats Main
    for i in range(1, 101):
        seat_row = math.ceil(i/10)
        if seat_row <= 2:
            seat_rank = vip
        elif seat_row <= 5:
            seat_rank = premium
        else:
            seat_rank = economy
        Seat.objects.get_or_create(number=i, section=main, row=seat_row, rank=seat_rank)
    
    # Add seats Rear
    for i in range(101, 151):
        seat_row = math.ceil((i-100)/10)
        if seat_row <= 2:
            seat_rank = vip
        elif seat_row <= 5:
            seat_rank = premium
        else:
            seat_rank = economy
        Seat.objects.get_or_create(number=i, section=rear, row=seat_row, rank=seat_rank)
    
    # Add seats Right
    for i in range(151, 201):
        seat_row = math.ceil((i-150)/10)
        if seat_row <= 2:
            seat_rank = vip
        elif seat_row <= 5:
            seat_rank = premium
        else:
            seat_rank = economy
        Seat.objects.get_or_create(number=i, section=right, row=seat_row, rank=seat_rank)

    # Add seats Left
    for i in range(201, 251):
        seat_row = math.ceil((i-200)/10)
        if seat_row <= 2:
            seat_rank = vip
        elif seat_row <= 5:
            seat_rank = premium
        else:
            seat_rank = economy
        Seat.objects.get_or_create(number=i, section=left, row=seat_row, rank=seat_rank)


if __name__ == "__main__":
    try:
        os.remove(settings.DATABASES['default']['NAME'])
    except:
        print('db does not exists, skip deletion')
    call_command("migrate", interactive=False)
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='',
            password='testpass123',
        )
    populate()