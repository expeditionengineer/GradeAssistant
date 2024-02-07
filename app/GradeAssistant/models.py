from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Student(models.Model):
    """Class reprenting the `Student`-Database-Table

    """
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    classRelation = models.ForeignKey("Class", on_delete=models.CASCADE)
    grades = models.ManyToManyField("Grade", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Class(models.Model):
    """Class representing the `Class`-Database table.

    """
    className = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Grade(models.Model):
    """Class representing the `Grade`-Database table.

    """
    points = models.IntegerField(default=0, choices=((i,i) for i in range(0, 15)), blank=True)
    weight = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], blank=True)
    parent = models.ForeignKey("Grade", on_delete=models.CASCADE, blank=True, null=True)
    students = models.ManyToManyField("Student")
    description = models.CharField(max_length=30, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)