# Generated by Django 3.1.4 on 2020-12-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel2', '0011_auto_20201222_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Updates',
            fields=[
                ('update', models.CharField(max_length=150, primary_key=True, serialize=False)),
            ],
        ),
    ]