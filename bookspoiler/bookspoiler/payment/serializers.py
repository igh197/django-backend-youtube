from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields=['id','user_id','challengeinfo_id','price','merchant_uid','created_at']