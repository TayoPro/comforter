# Generated by Django 4.2.1 on 2023-06-22 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0039_job_apply_admin_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_apply',
            name='admin_note',
            field=models.TextField(blank=True, null=True),
        ),
    ]