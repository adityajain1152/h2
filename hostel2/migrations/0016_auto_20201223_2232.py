# Generated by Django 3.0.5 on 2020-12-23 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel2', '0015_auto_20201223_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legends',
            name='year',
            field=models.IntegerField(max_length=150),
        ),
    ]
