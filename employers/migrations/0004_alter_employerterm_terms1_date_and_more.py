# Generated by Django 4.2.1 on 2023-05-19 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0003_alter_employerterms2_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employerterm',
            name='terms1_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='employerterms2',
            name='terms2_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
