# Generated by Django 4.2.6 on 2023-11-01 08:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_rename_comments_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(related_name='likeCount', to=settings.AUTH_USER_MODEL),
        ),
    ]