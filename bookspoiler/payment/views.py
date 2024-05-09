
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from payment.serializers import PaymentSerializer
import datetime
from iamport import Iamport
from rest_framework.renderers import JSONRenderer
#올릴떈 민감정보 숨기기

class PaymentView(APIView):

    renderer_classes = [JSONRenderer]

    def post(self,request):
        iamport= Iamport()
        payment = Payment.objects.create(
            user=request.user.nickname,
            challengeInfo=request.challenge_info_id,
            price=request.amount,
            timestamp=datetime.now(),
            merchant_uid=request.merchant_uid
        )
        response = iamport.payment(**payment)

        serializer = PaymentSerializer(response)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def delete(self,request):
        iamport=Iamport()
        data=request.data
        imp_uid= data.get('imp_uid')

        iamport.cancel(imp_uid=imp_uid)
        serializer = PaymentSerializer(data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    
    
    def get_payments(self):
        payment= Payment.objects.all()
        serializer = PaymentSerializer(payment,many=True)
        return Response(data=serializer.data)