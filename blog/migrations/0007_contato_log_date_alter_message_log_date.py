# Generated by Django 5.1.2 on 2024-12-10 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_contato_email_alter_message_log_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='log_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 10, 10, 5, 16, 193367)),
        ),
        migrations.AlterField(
            model_name='message',
            name='log_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 10, 10, 5, 16, 193367)),
        ),
    ]
