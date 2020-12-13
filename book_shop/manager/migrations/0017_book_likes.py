# Generated by Django 3.1.4 on 2020-12-13 10:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0016_auto_20201213_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_books', through='manager.LikeBookUser', to=settings.AUTH_USER_MODEL),
        ),
    ]