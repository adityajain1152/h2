# Generated by Django 3.0.5 on 2020-12-21 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel2', '0004_auto_20201221_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='council',
            name='councillor',
            field=models.BooleanField(default=False),
        ),
    ]
