# Generated by Django 4.2.1 on 2023-05-23 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0009_job_apply_new_applied'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_apply',
            name='notice_read',
            field=models.BooleanField(default=False),
        ),
    ]
