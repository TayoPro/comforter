# Generated by Django 4.2.1 on 2023-06-14 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_jobtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobtitle',
            name='list_item1',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='jobtitle',
            name='list_item2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='jobtitle',
            name='list_item3',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='jobtitle',
            name='list_item4',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='jobtitle',
            name='list_title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
