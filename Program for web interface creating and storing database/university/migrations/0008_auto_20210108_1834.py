# Generated by Django 3.0.7 on 2021-01-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0007_auto_20210108_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indexs',
            name='exams',
        ),
        migrations.AddField(
            model_name='indexs',
            name='exams',
            field=models.ManyToManyField(to='university.Exam'),
        ),
        migrations.RemoveField(
            model_name='indexs',
            name='professors',
        ),
        migrations.AddField(
            model_name='indexs',
            name='professors',
            field=models.ManyToManyField(to='university.Professor'),
        ),
        migrations.RemoveField(
            model_name='indexs',
            name='students',
        ),
        migrations.AddField(
            model_name='indexs',
            name='students',
            field=models.ManyToManyField(to='university.Student'),
        ),
    ]
