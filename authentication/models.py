from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Users(AbstractUser):
    uID=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='UID')
    #pass