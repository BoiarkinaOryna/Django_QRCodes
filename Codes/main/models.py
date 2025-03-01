from django.db import models
from django.contrib.auth.models import User

class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    subscription = models.CharField(max_length = 255)

# Create your models here.
