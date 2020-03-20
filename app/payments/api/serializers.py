from rest_framework import serializers
from payments.models import GuestPaymentInfo, HostPaymentInfo

class GuestPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestPaymentInfo
        fields = '__all__'

class HostPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostPaymentInfo
        fields = '__all__'

