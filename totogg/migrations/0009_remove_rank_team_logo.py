# Generated by Django 4.0.5 on 2022-07-08 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('totogg', '0008_rank_team_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rank',
            name='team_logo',
        ),
    ]
