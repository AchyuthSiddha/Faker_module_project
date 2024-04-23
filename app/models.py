from django.db import models

# Create your models here.
class Student(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=30)
    sdob=models.DateField()
    smarks=models.IntegerField()
    sphone=models.BigIntegerField()
    saddr=models.TextField()
    semail=models.EmailField()
