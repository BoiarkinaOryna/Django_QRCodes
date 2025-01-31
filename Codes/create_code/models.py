from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Code(models.Model):
    image_qr = models.ImageField(upload_to = '')
    title = models.CharField(max_length = 255)
    date_time = models.DateTimeField(auto_now_add = True)
    expire_date = models.DateTimeField() 
    costumization = models.CharField(max_length = 255)
    url = models.URLField()
    color = models.CharField(max_length = 40)
    bgcolour = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    description = models.TextField()
    center_image = models.ImageField(upload_to = '')