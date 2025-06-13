from rest_framework import serializers
from .models import Ticket, Booking
from accounts.models import CustomUser

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['ticket', 'name', 'phone', 'email']

    def validate_email(self, value):
        if not CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Please register before booking.")
        return value

    def create(self, validated_data):
        user = CustomUser.objects.get(email=validated_data['email'])
        return Booking.objects.create(user=user, **validated_data)

class BookingDetailSerializer(serializers.ModelSerializer):
    ticket = TicketSerializer()
    
    class Meta:
        model = Booking
        fields = ['id', 'ticket', 'name', 'phone', 'email']
