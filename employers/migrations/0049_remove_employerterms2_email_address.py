# Generated by Django 4.2.1 on 2023-06-09 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0048_alter_employer_profile_website'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employerterms2',
            name='email_address',
        ),
    ]
