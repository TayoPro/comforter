# Generated by Django 4.2.1 on 2023-05-22 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0024_alter_job_post_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_post',
            name='num',
        ),
    ]
