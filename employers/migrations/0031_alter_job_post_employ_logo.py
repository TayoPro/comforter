# Generated by Django 4.2.1 on 2023-05-23 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0030_job_post_employ_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_post',
            name='employ_logo',
            field=models.ImageField(upload_to='employer_profile'),
        ),
    ]
