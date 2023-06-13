from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Course(models.Model):
    department = models.ForeignKey(Department ,on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name



class Order(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    PURPOSE_CHOICES = (
        ('Enquiry', 'Enquiry'),
        ('Place Order', 'Place Order'),
        ('Return', 'Return'),
    )
    MATERIALS_CHOICES = (
        ('Notebook', 'Notebook'),
        ('Pen', 'Pen'),
        ('Exam Papers', 'Exam Papers'),
    )

    name=models.CharField(max_length=40)
    dob=models.DateField()
    age=models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phnumber = models.CharField(max_length=20)
    email=models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES)
    materials_provide = models.ManyToManyField('Materials')

    def __str__(self):
        return self.name

class Materials(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name