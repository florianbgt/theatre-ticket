from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from .models import Section, Rank, Seat
from fixture import populate
from .algo import main

import math
from random import randint

class TicketsTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        populate()
        self.sections = Section.objects.all()
        self.ranks = Rank.objects.all()
        self.seats = Seat.objects.all()
        self.availableSeats = Seat.objects.filter(blocked=False)

    def test_algo_1(self):
        nonUsedSeats = len(self.seats.filter(user=None))
        seats = main(self.sections, self.ranks, self.seats, [])
        self.assertEqual(len(self.seats.filter(user=None)), nonUsedSeats)
    
    def test_algo_2(self):
        available = len(self.availableSeats)
        main(self.sections, self.ranks, self.seats, [available])
        self.assertEqual(len(self.seats.filter(user=None)), len(self.seats)-available)

    def test_algo_3(self):
        available = len(self.availableSeats)
        groups = []
        while sum(groups) < available:
            max = available - sum(groups)
            groups.append(randint(1, max))
        main(self.sections, self.ranks, self.seats, groups)
        self.assertEqual(len(self.seats.filter(user=None)), len(self.seats)-available)

    def test_algo_4(self):
        available = len(self.availableSeats)
        groups = []
        while sum(groups) < available:
            max = available - sum(groups)
            groups.append(randint(1, max))
        main(self.sections, self.ranks, self.seats, groups)
        self.assertEqual(len(self.seats.filter(user=None)), len(self.seats)-available)
