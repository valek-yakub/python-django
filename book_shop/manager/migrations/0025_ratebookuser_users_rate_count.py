# Generated by Django 3.1.4 on 2020-12-16 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0024_auto_20201216_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratebookuser',
            name='users_rate_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
