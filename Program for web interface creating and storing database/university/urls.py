from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('professors', views.professors, name='professors'),
    path('students', views.students, name='students'),
    path('exams', views.exams, name='exams'),
]

