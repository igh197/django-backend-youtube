from django.urls import path
from .views import VideoDetail
from .views import(
   VideoList
)
urlpatterns = [
   path('',VideoList.as_view(),name='video-list'),
   path('<int:pk>',VideoDetail.as_view(),name='video-detail')
]