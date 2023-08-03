from django.db import models

# Create your models here.


from typing import Any
from django.db import models



class WeatherData(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    detailing_type = models.CharField(max_length=20)
    data = models.JSONField()
    last_updated = models.DateTimeField()



class Department(models.Model):
    department = models.CharField(max_length=100)

    


    
    def __str__(self):
        return self.department
    
    class Meta:
        ordering = ['department']



class StudentId(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self):
        return self.student_id


class Student(models.Model):
    department = models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentId, related_name="studentid", on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()


    

    def __str__(self):
        return self.student_name

    class Meta:
        ordering = ['student_name']
        verbose_name = ['student']

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.subject_name
    

class SubjectMarks(models.Model):
    student = models.ForeignKey(Student,related_name="studentmarks", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField(default=33)


    class Meta:
        unique_together = ['student', 'subject']

    def __str__(self) -> str:
        return f'{self.student.student_name} and {self.subject.subject_name}'


class studentCard(models.Model):
    student = models.ForeignKey(Student, related_name='student_rank', on_delete=models.CASCADE)
    rank = models.IntegerField(unique=True)
    date_of_generation = models.DateTimeField(auto_now_add=True)

class meta:
    unique_together = ['rank','date_of_generation']
