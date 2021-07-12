from django.db import models


# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=150, null=True)
    matriculation_number = models.IntegerField(default=0, null=True)

    def __str__(self):
        return "Student: {} {}".format(self.name, self.matriculation_number)


class Professor(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "Professor: {}".format(self.name)


class Exam(models.Model):
    topic = models.CharField(max_length=200, null=True)
    docent = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True)
    participants = models.ManyToManyField(Student, related_name="Exam")

    def __str__(self):
        return "Exam: {} ".format(self.topic)


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True)
    result = models.IntegerField(default=0, null=True)

    def __str__(self):
        return "Grade: {} for {} in {}".format(self.result, self.student, self.exam)
