# Generated by Django 4.2.1 on 2023-05-23 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0013_remove_job_apply_employer_profile_job_apply_job_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_apply',
            name='empl_logo',
            field=models.ImageField(blank=True, null=True, upload_to='employer_profile'),
        ),
    ]