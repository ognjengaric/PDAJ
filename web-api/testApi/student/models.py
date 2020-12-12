from django.db import models


# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    index = models.CharField(max_length=10, unique=True)
    year = models.IntegerField()

    def __str__(self):
        return self.index + " " + self.name + " " + self.last_name


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.CharField(max_length=30)
    value = models.IntegerField()

    def __str__(self):
        return str(self.student) + " " + self.course + " " + str(self.value)
