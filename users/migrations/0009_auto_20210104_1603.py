# Generated by Django 3.1.4 on 2021-01-04 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210101_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='e_certificates',
            field=models.ImageField(default='default_2.jpg', upload_to='profile_pics'),
        ),
    ]
