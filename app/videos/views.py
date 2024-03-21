from django.shortcuts import render
from rest_framework.views import APIView
from .models import Video
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .serializers import VideoListSerializer,VideoDetailSerializer
# Create your views here.
# Video와 관련된 restapi

#1.VideoList
#api/v1/video
#[GET]: 전체 비디오 목록 조회
#[POST]: 새로운 비디오 생성
class VideoList(APIView):
    def get(self,request):
        videos = Video.objects.all() #queryset video,video,video...
        serializers = VideoListSerializer(videos, many=True)#객체 2개 이상

        return Response(serializers.data,status.HTTP_200_OK)
    def post(self,request):
        user_data = request.data
        serializer=VideoListSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
#2.VideoDetail
#api/v1/video/{video_id}
#GET,PUT
    
class VideoDetail(APIView):
    def get(self,request,pk):
        try:
            video = Video.objects.get(pk=pk)
            
        except Video.DoesNotExist:
            raise NotFound
        serializer = VideoDetailSerializer(video)
        return Response(serializer.data,status.HTTP_200_OK)
    
    def put(self,request,pk):
        
        video_obj = Video.objects.get(pk=pk)
        user_data = request.data
        serializer = VideoDetailSerializer(video_obj,user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,pk):
        video_obj = Video.objects.get(pk=pk)
        video_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)