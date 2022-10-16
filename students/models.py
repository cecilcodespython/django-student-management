from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Student(models.Model):
    index_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    course = models.CharField(max_length=50)
    cwa = models.FloatField()

    def __str__(self) -> str:
        return f'Student: {self.first_name} {self.last_name }'