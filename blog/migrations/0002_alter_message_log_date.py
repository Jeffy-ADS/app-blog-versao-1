# Generated by Django 5.1.2 on 2024-12-09 12:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='log_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 9, 9, 53, 40, 652035)),
        ),
    ]