# Generated by Django 5.1.2 on 2024-12-09 12:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.CharField(default='Mensagem', max_length=500)),
                ('log_date', models.DateTimeField(default=datetime.datetime(2024, 12, 9, 9, 42, 36, 306463))),
            ],
        ),
    ]
