from django.urls import path
from .views import (
    TicketListCreateView,
    BookingCreateView,
    BookingListView,
    BookingByEmailView
)

urlpatterns = [
    path('tickets/', TicketListCreateView.as_view(), name='ticket-list'),
    path('book/', BookingCreateView.as_view(), name='book-ticket'),
    path('bookings/', BookingListView.as_view(), name='all-bookings'),
    path('bookings/<str:email>/', BookingByEmailView.as_view(), name='bookings-by-email'),
]
