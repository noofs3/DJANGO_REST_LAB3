from django.db import models

# Create your models here.
class Student(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    BirthDay = models.DateField()
    GPA = models.FloatField()