# Generated by Django 3.1.4 on 2020-12-16 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0027_auto_20201216_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='user_rate',
            field=models.FloatField(default=0.0, verbose_name='rate'),
        ),
    ]
