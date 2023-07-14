from django.db import models

# Create your models here.


class Attendance(models.Model):
    employee_number = models.IntegerField()
    check_in = models.DateTimeField(null=True)
    check_out = models.DateTimeField(null=True)