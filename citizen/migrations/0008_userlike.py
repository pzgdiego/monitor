# Generated by Django 2.2.13 on 2020-07-24 03:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('citizen', '0007_auto_20200723_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_authors', to=settings.AUTH_USER_MODEL)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_likes', to='citizen.Survey')),
            ],
        ),
    ]