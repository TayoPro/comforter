# Generated by Django 4.2.1 on 2023-06-14 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_jobtitle_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobtitle',
            name='list2_item1',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='jobtitle',
            name='list2_item2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='jobtitle',
            name='list2_item3',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='jobtitle',
            name='list2_item4',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='jobtitle',
            name='list2_item5',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='jobtitle',
            name='list2_item6',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='jobtitle',
            name='list2_item7',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='jobtitle',
            name='list2_title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
