# Generated by Django 3.1.4 on 2021-01-01 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20201228_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='interests',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
