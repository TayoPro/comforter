# Generated by Django 4.2.1 on 2023-05-24 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0020_job_apply_language_spoken_job_apply_previous_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_apply',
            name='language_spoken',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='job_apply',
            name='previous_company',
            field=models.CharField(max_length=250),
        ),
    ]
