# Generated by Django 4.2.2 on 2023-06-29 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
