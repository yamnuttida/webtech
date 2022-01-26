from django.db import models

# Create your models here.
class Faculty(models.Model):
    facname = models.CharField(max_length=225)

class Member(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=100)
    birthday = models.DateField("birthday date")
    facname = models.ForeignKey(Faculty,on_delete=models.CASCADE)
