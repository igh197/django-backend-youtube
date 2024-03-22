from rest_framework import serializers
from .models import Video
from users.serializers import UserSerializer
from comments.serializers import CommentSerializer
from reactions.models import Reaction
class VideoListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Video
        fields = '__all__'


class VideoDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    comment_set = CommentSerializer(read_only=True,many=True)
    reactions = serializers.SerializerMethodField()
    class Meta:
        model = Video
        fields = '__all__'
    def get_reactions(self,video):
        return Reaction.get_video_reaction(video)
        
        
      
