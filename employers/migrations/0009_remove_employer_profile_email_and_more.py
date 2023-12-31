# Generated by Django 4.2.1 on 2023-05-19 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employers', '0008_alter_employerpayment_employer_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer_profile',
            name='email',
        ),
        migrations.AlterField(
            model_name='employer_profile',
            name='about_us',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='employer_profile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
