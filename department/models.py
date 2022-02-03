from django.db import models
from djmoney.models.fields import MoneyField


class Department(models.Model):
    department_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60, null=True)
    budget = MoneyField(null=False, max_digits=20)
    start_date = models.DateField(null=False)
    instructor = models.ForeignKey('person.Person', null=True, on_delete=models.CASCADE)
