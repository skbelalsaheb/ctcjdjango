from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.IntegerField(max_length=10)
    batch = models.CharField(max_length=255)
    sid = models.CharField(max_length=255)
    stream = models.CharField(max_length=255)




