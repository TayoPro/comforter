# Generated by Django 4.2.1 on 2023-05-22 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0013_job_post_employer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_post',
            name='employer_name',
            field=models.CharField(max_length=50),
        ),
    ]
