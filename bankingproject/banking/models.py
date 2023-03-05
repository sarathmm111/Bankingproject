from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
class District(models.Model):
    districtname = models.CharField(max_length=250)

    def __str__(self):
        return self.districtname


class Branch(models.Model):
    distid = models.ForeignKey(District, on_delete=CASCADE)
    branch = models.CharField(max_length=250)

    def __str__(self):
        return self.branch


class Person(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField(default=None)
    age = models.IntegerField(default=None)
    gender = models.CharField(max_length=50, choices=(('Male', 'Male'), ('Female', 'Female'),))
    phone = models.CharField(max_length=10, default=None)
    email = models.EmailField()
    address = models.TextField(max_length=250)
    district = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    account = models.CharField(max_length=50)
    material = models.CharField(max_length=50)

    def __str__(self):
        return self.name
