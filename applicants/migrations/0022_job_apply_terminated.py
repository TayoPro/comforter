# Generated by Django 4.2.1 on 2023-05-25 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0021_alter_job_apply_language_spoken_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_apply',
            name='terminated',
            field=models.BooleanField(default=False),
        ),
    ]
