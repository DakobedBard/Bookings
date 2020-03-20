from rest_framework import serializers
from reservations.models import Reservation

class ReserverationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


