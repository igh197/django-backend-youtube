from django.db import models
from user.models import User
from challengeinfo.models import ChallengeInfo
# Create your models here.
class Payment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    challenge_info=models.ForeignKey(ChallengeInfo,on_delete=models.CASCADE)
    price = models.IntegerField(default=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='payment'
