# Generated by Django 3.1.4 on 2020-12-13 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0017_book_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeCommentUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveConstraint(
            model_name='likebookuser',
            name='unique_like',
        ),
        migrations.AlterField(
            model_name='likebookuser',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_user_table', to='manager.book'),
        ),
        migrations.AlterField(
            model_name='likebookuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_book_table', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='likebookuser',
            constraint=models.UniqueConstraint(fields=('book', 'user'), name='like_unique_book_user'),
        ),
        migrations.AddField(
            model_name='likecommentuser',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_user_table', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='likecommentuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_comment_table', to='manager.comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_comments', through='manager.LikeCommentUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='likecommentuser',
            constraint=models.UniqueConstraint(fields=('comment', 'user'), name='like_unique_comment_user'),
        ),
    ]
