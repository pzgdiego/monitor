# Generated by Django 2.2.13 on 2020-07-23 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0004_auto_20200719_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='supply_time',
            field=models.IntegerField(choices=[(0, 'null'), (1, 'Less than 6 Hours per week'), (2, 'More than 6 hours but less than 24 hours this week'), (3, 'More than 24 hours this week')]),
        ),
    ]
