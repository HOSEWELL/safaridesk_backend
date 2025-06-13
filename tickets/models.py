from django.db import models
from django.conf import settings

class Ticket(models.Model):
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_of_departure = models.DateField()

    def __str__(self):
        return f"{self.departure} → {self.destination} on {self.date_of_departure}"

class Booking(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()  # For lookup

    def __str__(self):
        return f"{self.name} booked {self.ticket}"
