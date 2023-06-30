# Generated by Django 4.2.2 on 2023-06-29 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0004_tasks_tags_remove_tasks_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks_tags',
            name='tag_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tasks.tags'),
        ),
        migrations.AlterField(
            model_name='tasks_tags',
            name='task_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tasks.tasks'),
        ),
    ]