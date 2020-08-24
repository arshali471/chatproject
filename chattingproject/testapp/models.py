from django.db import models
from django.utils.timezone import now

# Create your models here.
class MessageModel(models.Model):
    message=models.CharField(max_length=10000)
    user_name=models.CharField(max_length=256)
    time=models.DateTimeField(auto_now_add=True)
