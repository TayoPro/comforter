# Generated by Django 4.2.1 on 2023-05-22 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0011_rename_new_job_post_job_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer_profile',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
