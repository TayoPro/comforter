# Generated by Django 4.2.1 on 2023-05-22 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0027_alter_job_post_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_post',
            name='publish',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='job_post',
            name='job_open',
            field=models.BooleanField(default=False),
        ),
    ]
