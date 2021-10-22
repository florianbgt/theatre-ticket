
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import Seat
from .serializers import SeatSerializer, AssignSeatsSerializer
from .algo import main

class SeatList(generics.ListAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class SeatDetail(generics.RetrieveAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class AssignSeats(APIView):
    def post(self, request):
        serializer = AssignSeatsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            groups = serializer.save()['groups']
        seats = main(groups)
        return Response(seats)