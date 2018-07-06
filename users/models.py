from django.db import models
from django.contrib.auth.models import User
 
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, related_name='user')
#     phone = models.CharField(max_length=20, blank=True, default='')
#     about = models.TextField(default='', blank=True)