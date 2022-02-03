from django.db import models


class Enrollment(models.Model):
    enrollment_id = models.IntegerField(primary_key=True)
    course = models.ForeignKey('course.Course', null=False, on_delete=models.CASCADE)
    student_id = models.ForeignKey('person.Person', null=False, on_delete=models.CASCADE)
    grade = models.IntegerField(null=True)

