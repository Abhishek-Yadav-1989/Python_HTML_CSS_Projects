# Generated by Django 3.0.7 on 2021-01-07 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0004_auto_20210108_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='participants',
            field=models.ManyToManyField(related_name='Exam', to='university.Student'),
        ),
    ]
