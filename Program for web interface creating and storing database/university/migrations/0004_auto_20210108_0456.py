# Generated by Django 3.0.7 on 2021-01-07 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0003_auto_20210108_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='participants',
            field=models.ManyToManyField(to='university.Student'),
        ),
    ]
