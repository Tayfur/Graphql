# Generated by Django 3.1.3 on 2020-12-01 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=120)),
                ('model', models.CharField(max_length=120)),
                ('year', models.CharField(max_length=10)),
            ],
        ),
    ]
