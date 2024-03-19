from django.db import models
from common.models import CommonModel
from users.models import User
# Create your models here.
class Video(CommonModel):
    title = models.CharField(max_length=30,required=True)
    description = models.TextField(blank=True)
    link = models.URLField()
    category = models.CharField(max_length=20)
    views_count = models.PositiveIntegerField(default = 0)
    thumbnail = models.URLField()
    video_file = models.FileField(upload_to='storage/')
    
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)