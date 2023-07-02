# Generated by Django 4.2.1 on 2023-06-01 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0045_alter_employerpayment_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employerterms2',
            name='client_name',
        ),
        migrations.AddField(
            model_name='employerterms2',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='employerterms2',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
    ]