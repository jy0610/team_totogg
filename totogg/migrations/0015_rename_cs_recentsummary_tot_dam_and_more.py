# Generated by Django 4.0.5 on 2022-07-11 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('totogg', '0014_alter_gameschedule_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recentsummary',
            old_name='cs',
            new_name='tot_dam',
        ),
        migrations.RenameField(
            model_name='recentsummary',
            old_name='dam',
            new_name='total_cs',
        ),
    ]
