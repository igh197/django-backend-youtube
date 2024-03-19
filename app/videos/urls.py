from django.urls import path
from .views import(
   VideoList
)
urlpatterns = [
   path('',VideoList.as_view(),name='video-list')
]