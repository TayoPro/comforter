# Generated by Django 4.2.1 on 2023-05-25 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0035_remove_job_post_job_dat_remove_job_post_job_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_post',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
