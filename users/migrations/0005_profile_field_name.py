# Generated by Django 3.1.4 on 2020-12-27 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='field_name',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
