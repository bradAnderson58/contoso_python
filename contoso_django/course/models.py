from django.db import models


class Course(models.Model):
    course_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=60, null=True)
    credits = models.IntegerField(null=False)
    department = models.ForeignKey('department.Department', null=False, default=1, on_delete=models.CASCADE)
    instructors = models.ManyToManyField('person.Person', related_name='courses', db_table='course_instructor')
