# Generated by Django 4.2.2 on 2023-06-29 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0002_tasks_finished'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='tag',
        ),
        migrations.AddField(
            model_name='tasks',
            name='tag',
            field=models.ManyToManyField(to='Tasks.tags'),
        ),
    ]
