# Generated by Django 4.1.3 on 2022-11-24 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_destination_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='desc',
            field=models.CharField(max_length=100),
        ),
    ]
