# Generated by Django 3.0.5 on 2020-12-20 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Legend_Category',
            fields=[
                ('name', models.CharField(max_length=150, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Legends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('year', models.CharField(max_length=150)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel2.Legend_Category')),
            ],
        ),
    ]