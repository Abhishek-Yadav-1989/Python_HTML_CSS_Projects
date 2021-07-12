from django.shortcuts import render

from .models import *


# Create your views here.
def index(request):
    professors = Professor.objects.all()
    students = Student.objects.all()
    exams = Exam.objects.all()
    context = {"professors": professors, "students": students, "exams": exams}
    return render(request, 'university/index.html', context)


def professors(request):
    professors = Professor.objects.all()
    context = {"professors": professors}
    return render(request, 'university/professors.html', context)


def students(request):
    students = Student.objects.all()
    context = {"students": students}
    return render(request, 'university/students.html', context)


def exams(request):
    exams = Exam.objects.all()
    context = {"exams": exams}
    return render(request, 'university/exams.html', context)
