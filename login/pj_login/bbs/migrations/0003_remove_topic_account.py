# Generated by Django 3.1.14 on 2022-06-06 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0002_topic_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='account',
        ),
    ]