# Generated by Django 4.2.1 on 2023-05-29 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_category_cat_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'managed': True, 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
    ]
