# Generated by Django 4.2.1 on 2023-05-24 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0019_alter_general_information_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_apply',
            name='language_spoken',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='job_apply',
            name='previous_company',
            field=models.CharField(default='', max_length=250),
        ),
    ]