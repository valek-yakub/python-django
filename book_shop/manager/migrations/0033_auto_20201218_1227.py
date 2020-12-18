# Generated by Django 3.1.4 on 2020-12-18 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0032_auto_20201218_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='users_rate_score',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2, verbose_name='rate'),
        ),
        migrations.AlterField(
            model_name='ratebookuser',
            name='user_rate_score',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2, verbose_name='user_book_rate'),
        ),
    ]
