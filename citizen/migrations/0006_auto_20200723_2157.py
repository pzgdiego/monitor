# Generated by Django 2.2.13 on 2020-07-24 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0005_auto_20200722_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='supply_time',
            field=models.IntegerField(choices=[(1, 'Less than 6 Hours per week'), (2, 'More than 6 hours but less than 24 hours this week'), (3, 'More than 24 hours this week')]),
        ),
    ]