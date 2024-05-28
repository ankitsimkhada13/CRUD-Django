from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)