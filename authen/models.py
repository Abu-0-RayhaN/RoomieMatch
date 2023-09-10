from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    nid = models.CharField(max_length=17,unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    objects = UserManager()
    REQUIRED_FIELDS=[]
    USERNAME_FIELD = 'email'
    class Meta:
        app_label = 'authen'

    

