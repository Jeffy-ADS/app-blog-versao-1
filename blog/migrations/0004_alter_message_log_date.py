# Generated by Django 5.1.2 on 2024-12-09 14:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_contato_alter_message_log_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='log_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 9, 11, 35, 3, 940504)),
        ),
    ]