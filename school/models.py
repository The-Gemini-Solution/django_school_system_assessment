from ctypes import POINTER
from typing import Optional

from django.db import models

# Create your models here.
class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    subject_speciality = models.CharField(max_length=20)

    @property
    def first_name(self) -> Optional[str]:
        raise NotImplementedError

    @property
    def middle_name(self) -> Optional[str]:
        raise NotImplementedError

    @property
    def surname(self) -> Optional[str]:
        raise NotImplementedError


class Enrollment(models.Model):
    school_class = models.ForeignKey("school.Class", on_delete=models.CASCADE)
    student = models.ForeignKey("school.Student", on_delete=models.CASCADE)
    has_completed_class = models.BooleanField(null=False)
    score = models.PositiveSmallIntegerField()

    @property
    def grade(self) -> str:
        """
        Calculates the student's grade for the class using the following algorithm:
            has completed = False -> 'N/C'
            score > 80: A
            score > 75: B
            score > 70: C
            else F
        """

        if 100 >= self.score >= 80:
            return "A"
        elif 80 >= self.score >= 75:
            return "B"
        elif 75 >= self.score >= 70:
            return "C"

        if not self.has_completed_class:
            return "N/C"
        else:
            return "F"


class Class(models.Model):
    class_time = models.TimeField(auto_now=False, auto_now_add=False)
    class_subject = models.CharField(max_length=20)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL)
    students = models.ManyToManyField("school.Student", through=Enrollment)


class Student(models.Model):
    full_name = models.CharField(max_length=20)
    classes = models.ManyToManyField("school.Class", through=Enrollment)
