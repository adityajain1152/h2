# Generated by Django 3.1.4 on 2020-12-23 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel2', '0013_auto_20201223_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='updates',
            name='name',
            field=models.CharField(default='New Update', max_length=150, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='updates',
            name='update',
            field=models.CharField(default='No new Updates', max_length=150),
        ),
    ]