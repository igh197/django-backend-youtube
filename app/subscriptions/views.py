from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from subscriptions.serializers import SubSerializer
from subscriptions.models import Subscription
from django.shortcuts import get_object_or_404
from rest_framework import status
# Create your views here.
#POST 구독 신청
class SubscriptionList(APIView):
    #GET 내가 구독한 유튜버 리스트
    def get(self,request):
        subs = Subscription.objects.filter(subscriber=request.user)
        serializer = SubSerializer(subs,many=True)
        return Response(serializer.data)
    def post(self,request):
        user_data = request.data
        serializer = SubSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save(subscriber=request.user)
        return Response(serializer.data,201)

class SubscriptionDetail(APIView):
    def get(self,request,pk):
        subs = Subscription.objects.filter(subscribed_to=pk)
        serializer = SubSerializer(subs,many=True)
        return Response(serializer.data)

    def delete(self,request,pk):
        sub=get_object_or_404(Subscription,pk=pk,subscriber = request.user)
        sub.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)