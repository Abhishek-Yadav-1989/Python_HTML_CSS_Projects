# Generated by Django 3.0.7 on 2021-01-07 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_auto_20200623_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='participants',
            field=models.ManyToManyField(related_name='Exam', to='university.Student'),
        ),
    ]
