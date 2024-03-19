from django.shortcuts import render
from rest_framework.views import APIView
from .models import Video
from .serializers import VideoSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
# Video와 관련된 restapi

#1.VideoList
#api/v1/video
#[GET]: 전체 비디오 목록 조회
#[POST]: 새로운 비디오 생성
class VideoList(APIView):
    def get(self):
        videos = Video.objects.all() #queryset video,video,video...
        serializers = VideoSerializer(videos, many=True)#객체 2개 이상
        return Response(serializers.data,status.HTTP_200_OK)
    def post(self,request):
        user_data = request.data
        serializer=VideoSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
#2.VideoDetail
#api/v1/video/{video_id}
#GET,PUT
    
class VideoDetail():
    def get():
        pass

    def post():
        pass