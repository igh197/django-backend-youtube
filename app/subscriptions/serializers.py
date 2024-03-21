from rest_framework import serializers
from .models import Subscription
class SubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

    #내가 나를 구독 불가능
    def validate(self,data):
        if data['subscriber'] == data['subscribed_to']:
            raise serializers.ValidationError("You can't not subscribe to yourself.")
        
        return data