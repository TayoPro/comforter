# Generated by Django 4.2.1 on 2023-05-29 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0029_alter_applicantpayment_total'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job_apply',
            options={'managed': True, 'verbose_name': 'Job_Apply', 'verbose_name_plural': 'Job_Apply'},
        ),
        migrations.AlterModelTable(
            name='job_apply',
            table='job_apply',
        ),
    ]