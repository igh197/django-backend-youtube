from django.db import models
from common.models import CommonModel
# Create your models here.
from django.db.models import Count,Q
class Reaction(CommonModel):
    user= models.ForeignKey('users.User',on_delete=models.CASCADE,related_name= 'users')
    video = models.ForeignKey('videos.Video',on_delete=models.CASCADE,related_name = 'videos')
    
    LIKE =1
    DISLIKE=-1
    NO_REACTION=0

    REACTION_CHOICES=(
        (LIKE,'Like'),
        (DISLIKE,'DisLike'),
        (NO_REACTION,'No Reaction')
    )
    
    reaction = models.IntegerField(choices=REACTION_CHOICES,default=NO_REACTION)

    @staticmethod
    def get_video_reaction(video):
        reactions = Reaction.objects.filter(video=video).aggregate(
            likes_count = Count('pk',filter=Q(reaction=Reaction.LIKE)),
            dislikes_count = Count('pk',filter=Q(reaction=Reaction.DISLIKE)),
        )
        return reactions
