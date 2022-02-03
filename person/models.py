from django.db import models


class Person(models.Model):
    last_name = models.CharField(max_length=50, null=False)
    first_name = models.CharField(max_length=50, null=False)
    hire_date = models.DateField(null=True)
    enrollment_date = models.DateField(null=True)
    discriminator = models.CharField(max_length=128, default='Instructor', null=False)


class OfficeAssignment(models.Model):
    instructor = models.ForeignKey('person.Person', null=False, on_delete=models.CASCADE)
    location = models.CharField(max_length=50, null=True)
