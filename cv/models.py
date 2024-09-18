from django.db import models

# Create your models here.
class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # null if currently employed

    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # null if currently employed

    def __str__(self):
        return f"{self.position} at {self.company}"

class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField()  # e.g., scale of 1-10

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
