# Generated by Django 4.0.5 on 2022-07-04 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('totogg', '0003_rank'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rank',
            old_name='teascore_scd',
            new_name='score_scd',
        ),
    ]
