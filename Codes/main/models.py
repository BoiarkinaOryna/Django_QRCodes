from django.db import models
from django.contrib.auth.models import User

class Subsciption(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    subsciption = models.CharField(max_length = 255)

# Create your models here.
