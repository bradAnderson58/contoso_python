from django.db import models


class Enrollment(models.Model):
    course = models.ForeignKey('course.Course', null=False, on_delete=models.CASCADE)
    student_id = models.ForeignKey('person.Person', null=False, on_delete=models.CASCADE)
    grade = models.IntegerField(null=True)

