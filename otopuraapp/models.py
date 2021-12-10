from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.



class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True)
    age = models.IntegerField(null=True, blank=True, default=0)
    genre = models.CharField(max_length=30, blank=True) 
    address = models.CharField(max_length=30, blank=True) 
    artist = models.CharField(max_length=30, blank=True)
    part =  models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to="")

class HostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    #image = models.ImageField(upload_to='')
    age = models.IntegerField(null=True, blank=True, default=0)
    email = models.EmailField(max_length=240)
    good_counts = models.IntegerField(null=True, blank=True, default=0)
    #event情報
    location = models.CharField(max_length=30, blank=True) 
    member = models.IntegerField(null=True, blank=True, default=0)
    event_date = models.DateField(null=True, blank=True)
    event_time = models.TimeField(null=True, blank=True)


class BandModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True)
    age = models.CharField(max_length=20, blank=True)
    genre = models.CharField(max_length=20, blank=True)
    part = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to="")
    good = models.IntegerField(null=True, blank=True, default=0)

class GoodModel(models.Model):
    #いいねされた人
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    #いいねした人
    good_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="good_user")
    name = models.CharField(max_length=20, blank=True)
    age = models.IntegerField(null=True, blank=True, default=0)
    genre = models.CharField(max_length=30, blank=True) 
    address = models.CharField(max_length=30, blank=True) 
    artist = models.CharField(max_length=30, blank=True)
    part =  models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to="")

class CommentModel(models.Model):
    #コメントした人
    cm_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cm_user")
    #コメントされた人
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cm_user_1")
    #コメント内容
    comment = models.TextField(
        verbose_name='',
        blank=True,
        null=True,
        max_length=1000,
    )
class DMModel(models.Model):
    #DMした人
    dm_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dm_user")
    #DMされた人
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dm_user_1")
    #DM内容
    dm = models.TextField(
        verbose_name='',
        blank=True,
        null=True,
        max_length=1000,
    )



