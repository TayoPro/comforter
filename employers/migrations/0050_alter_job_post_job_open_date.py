# Generated by Django 4.2.1 on 2023-06-09 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0049_remove_employerterms2_email_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_post',
            name='job_open_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
