# Generated by Django 3.1.4 on 2020-12-22 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel2', '0010_auto_20201222_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='cultcouncil',
            name='left',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='eventscouncil',
            name='left',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='maintcouncil',
            name='left',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='messcouncil',
            name='left',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sportscouncil',
            name='left',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='techcouncil',
            name='left',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='webcouncil',
            name='left',
            field=models.BooleanField(default=True),
        ),
    ]