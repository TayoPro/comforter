# Generated by Django 4.2.1 on 2023-05-26 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('applicants', '0027_rename_category_job_apply_category_apply'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('applicant_number', models.CharField(blank=True, max_length=250, null=True)),
                ('pay_code', models.CharField(blank=True, max_length=250, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=250, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('complete', models.BooleanField(default=False)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ApplicantPayment',
                'verbose_name_plural': 'ApplicantPayments',
                'db_table': 'applicantpayment',
                'managed': True,
            },
        ),
    ]
