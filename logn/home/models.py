from django.db import models

# Create your models here.


class Student(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=20)
    place = models.CharField(max_length=30)
    dept = models.CharField(max_length=20)


class Emp(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=20)

class Sigh(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    pwd = models.CharField(max_length=30)