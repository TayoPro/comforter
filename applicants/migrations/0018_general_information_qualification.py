# Generated by Django 4.2.1 on 2023-05-24 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0017_alter_job_apply_employer'),
    ]

    operations = [
        migrations.AddField(
            model_name='general_information',
            name='qualification',
            field=models.CharField(default='', max_length=250),
        ),
    ]
