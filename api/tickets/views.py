
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import Section, Rank, Seat
from .serializers import SectionSerializer, RankSerializer, SeatSerializer, AssignSeatsSerializer, GetSeatsSerializer
from .algo import main

class SectionList(generics.ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class RankList(generics.ListAPIView):
    queryset = Rank.objects.all()
    serializer_class = RankSerializer


class SeatList(generics.ListAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class AssignSeats(APIView):
    def post(self, request):
        serializer = AssignSeatsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            groups = serializer.save()['groups']
        sections = Section.objects.all()
        ranks = Rank.objects.all()
        seats = Seat.objects.all()
        main(sections, ranks, seats, groups)
        return Response(SeatSerializer(seats, many=True).data)


class GetSeats(APIView):
    def post(self, request):
        serializer = GetSeatsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            groups = serializer.save()['group']
        seats = Seat.objects.filter(user=groups)
        return Response(SeatSerializer(seats, many=True).data)