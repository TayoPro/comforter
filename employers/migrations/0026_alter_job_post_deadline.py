# Generated by Django 4.2.1 on 2023-05-22 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0025_remove_job_post_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_post',
            name='deadline',
            field=models.CharField(default='', max_length=250),
        ),
    ]
