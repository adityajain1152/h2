# Generated by Django 3.1.4 on 2020-12-22 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel2', '0006_auto_20201222_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='admincouncil',
            name='left',
            field=models.BooleanField(default=True),
        ),
    ]
