from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
# class dashboard(models.Model):
#     user = models.ForeignKey(User , on_delete = models.SET_NULL, null = True, blank = True)
#     # phone = models.CharField(max_length=10, blank=True, null=True)

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    full_name = models.CharField(max_length=50, blank= True, null=True)