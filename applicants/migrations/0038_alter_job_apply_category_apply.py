# Generated by Django 4.2.1 on 2023-06-09 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0037_alter_job_apply_deadline_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_apply',
            name='category_apply',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]