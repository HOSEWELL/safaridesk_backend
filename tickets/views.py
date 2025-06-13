from rest_framework import generics
from .models import Ticket, Booking
from .serializers import TicketSerializer, BookingSerializer, BookingDetailSerializer

class TicketListCreateView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingListView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer

class BookingByEmailView(generics.ListAPIView):
    serializer_class = BookingDetailSerializer

    def get_queryset(self):
        email = self.kwargs['email']
        return Booking.objects.filter(email=email)
