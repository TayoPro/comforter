# Generated by Django 4.2.1 on 2023-06-11 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0053_alter_job_post_job_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer_profile',
            name='website',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]
