# Generated by Django 3.1.4 on 2020-12-18 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0033_auto_20201218_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rate_stars_num',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='Number of checked stars'),
        ),
        migrations.AlterField(
            model_name='book',
            name='users_rate_count',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='Number of users, who rated.'),
        ),
    ]
