# Generated by Django 4.2.1 on 2023-06-14 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_jobtitle_list_item1_jobtitle_list_item2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobtitle',
            name='list_item5',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='jobtitle',
            name='list_item6',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='jobtitle',
            name='list_item7',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
